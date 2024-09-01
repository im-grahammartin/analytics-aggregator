from google.analytics.data_v1beta.types import (
    Dimension,
    Metric,
)

def build_metrics(metrics_str):
    metrics = []
    
    print(Metric)
    for metric in metrics_str.split(','):
        metrics.append(Metric(name=metric.strip()))
    
    return metrics

def build_dimensions(dimensions_str):
    dimensions = []

    if(type(dimensions_str) == str):
        for dimension in dimensions_str.split(','):
            dimensions.append(Dimension(name=dimension.strip()))
    
    return dimensions
