import pytest

from helpers.aggregator import aggregate_reports

# Combine two lists with properties in the same order
def test_aggregator_simple():
    # Arrange - set up input and expected output
    expected_length = 1
    expected_property = 'users'
    expected_value = 523
    expected_type = dict

    full_data = [{
        'name': 'Test Site 1',
        'results': [{
            'metrics': {
                'users': 123,    
            },
        }],
    },{
        'name': 'Test Site 1',
        'results': [{
            'metrics': {
                'users': 400,    
            },
        }],
    }]

    # Act
    aggregated_data = aggregate_reports(full_data)

    # Assert
    assert type(aggregated_data) == expected_type
    assert len(aggregated_data) == expected_length
    assert expected_property in aggregated_data
    assert aggregated_data[expected_property] == expected_value

# Combine two lists with multiple properties
def test_aggregator_multiple():
    # Arrange - set up input and expected output
    expected_length = 2
    expected_property_1 = 'users'
    expected_property_2 = 'pageViews'
    expected_users_value = 523
    expected_pageviews_value = 13960
    expected_type = dict

    full_data = [{
        'name': 'Test Site 1',
        'results': [{
            'metrics': {
                'users': 123,
                'pageViews': 9435,
            },
        }],
    },{
        'name': 'Test Site 1',
        'results': [{
            'metrics': {
                'users': 400,    
                'pageViews': 4525,
            },
        }],
    }]

    # Act
    aggregated_data = aggregate_reports(full_data)

    # Assert
    assert type(aggregated_data) == expected_type
    assert len(aggregated_data) == expected_length
    assert expected_property_1 in aggregated_data
    assert expected_property_2 in aggregated_data
    assert aggregated_data[expected_property_1] == expected_users_value
    assert aggregated_data[expected_property_2] == expected_pageviews_value

# Combine two lists with differing metrics
def test_aggregator_metric_mismatch():
    # Arrange - set up input and expected output
    expected_length = 2
    expected_property_1 = 'users'
    expected_property_2 = 'pageViews'
    expected_users_value = 400
    expected_pageviews_value = 9435
    expected_type = dict

    full_data = [{
        'name': 'Test Site 1',
        'results': [{
            'metrics': {
                'pageViews': 9435,
            },
        }],
    },{
        'name': 'Test Site 1',
        'results': [{
            'metrics': {
                'users': 400,    
            },
        }],
    }]

    # Act
    aggregated_data = aggregate_reports(full_data)

    # Assert
    assert type(aggregated_data) == expected_type
    assert len(aggregated_data) == expected_length
    assert expected_property_1 in aggregated_data
    assert expected_property_2 in aggregated_data
    assert aggregated_data[expected_property_1] == expected_users_value
    assert aggregated_data[expected_property_2] == expected_pageviews_value

# Combine two lists with a dimension
def test_aggregator_metric_with_dimension():
    # Arrange - set up input and expected output
    expected_length = 1
    expected_metric = 'users'
    expected_metric_value = 523
    expected_dimension_value = 'web'
    expected_type = dict

    full_data = [{
        'name': 'Test Site 1',
        'results': [{
            'dimensions': {
                'platform': 'web',
            },
            'metrics': {
                'users': 123,    
            },
        }],
    },{
        'name': 'Test Site 1',
        'results': [{
            'dimensions': {
                'platform': 'web',
            },
            'metrics': {
                'users': 400,    
            },
        }],
    }]

    # Act
    aggregated_data = aggregate_reports(full_data)

    # Assert
    assert type(aggregated_data) == expected_type
    assert len(aggregated_data) == expected_length
    assert expected_dimension_value in aggregated_data
    assert expected_metric in aggregated_data[expected_dimension_value]
    assert aggregated_data[expected_dimension_value][expected_metric] == expected_metric_value

# Combine multiple lists with multiple dimensions
def test_aggregator_metric_with_multiple_dimensions():
    # Arrange - set up input and expected output
    expected_length = 2
    expected_metric = 'users'
    expected_metric_1_value = 700
    expected_metric_2_value = 100
    expected_dimension_1_value = 'web|United Kingdom'
    expected_dimension_2_value = 'web|United States'
    expected_type = dict

    full_data = [{
        'name': 'Test Site 1',
        'results': [{
            'dimensions': {
                'platform': 'web',
                'country': 'United Kingdom',
            },
            'metrics': {
                'users': 500,    
            },
        }],
    },{
        'name': 'Test Site 2',
        'results': [{
            'dimensions': {
                'platform': 'web',
                'country': 'United Kingdom',
            },
            'metrics': {
                'users': 200,    
            },
        }],
    },{
        'name': 'Test Site 3',
        'results': [{
            'dimensions': {
                'platform': 'web',
                'country': 'United States',
            },
            'metrics': {
                'users': 100,    
            },
        }],
    }]

    # Act
    aggregated_data = aggregate_reports(full_data)

    # Assert
    assert type(aggregated_data) == expected_type
    assert len(aggregated_data) == expected_length
    assert expected_dimension_1_value in aggregated_data
    assert expected_dimension_2_value in aggregated_data
    assert expected_metric in aggregated_data[expected_dimension_1_value]
    assert expected_metric in aggregated_data[expected_dimension_2_value]
    assert aggregated_data[expected_dimension_1_value][expected_metric] == expected_metric_1_value
    assert aggregated_data[expected_dimension_2_value][expected_metric] == expected_metric_2_value
    