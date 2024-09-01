from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

def build_metrics(metrics_str):
    metrics = []
    
    for metric in metrics_str.split(','):
        metrics.append(Metric(name=metric.strip()))
    
    return metrics

def build_dimensions(dimensions_str):
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
        date_ranges=[DateRange(start_date=start_date, end_date=end_date)],
    )

def generate_ga_report(property_id, start_date, end_date, metrics, dimensions=None):
    client = BetaAnalyticsDataClient()
    request = build_report_request(property_id, start_date, end_date, metrics, dimensions)
    response = client.run_report(request)

    return response


