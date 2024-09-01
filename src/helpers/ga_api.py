from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

def build_metrics(metrics_str):
    # Available metrics: https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#metrics
    metrics = []
    
    for metric in metrics_str.split(','):
        metrics.append(Metric(name=metric.strip()))
    
    return metrics

def build_dimensions(dimensions_str):
    # Available dimensions: https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#dimensions
    dimensions = []

    if(type(dimensions_str) == str):
        for dimension in dimensions_str.split(','):
            dimensions.append(Dimension(name=dimension.strip()))
    
    return dimensions

def build_report_request(property_id, start_date, end_date, metrics_str, dimensions_str=None):
    return RunReportRequest(
        property=f'properties/{property_id}',
        metrics=build_metrics(metrics_str),
        dimensions=build_dimensions(dimensions_str),
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)], # Data range support: https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/DateRange
    )

def clean_ga_response(response):
    cleaned_response = []

    for row_index, row in enumerate(response.rows):
        new_dimensions = {}
        new_metrics = {}

        for dimension_index, dimension in enumerate(response.dimension_headers):
            new_dimensions[dimension.name] = row.dimension_values[dimension_index].value
            
        for metric_index, metric in enumerate(response.metric_headers):
            new_metrics[metric.name] = int(row.metric_values[metric_index].value)
        
        if(len(new_dimensions) == 0):
            cleaned_response = cleaned_response + [{ 'metrics': new_metrics }]
        else:
            cleaned_response = cleaned_response + [{ 'dimensions': new_dimensions, 'metrics': new_metrics }]    

    return cleaned_response

def generate_ga_report(property_id, start_date, end_date, metrics, dimensions=None):
    client = BetaAnalyticsDataClient()

    # Build a fully formed GA request compatible with GA Data API
    request = build_report_request(property_id, start_date, end_date, metrics, dimensions)

    # Request the report
    response = client.run_report(request)

    # Clean the response to suit our needs
    clean_response = clean_ga_response(response)

    print(clean_response)

    return clean_response