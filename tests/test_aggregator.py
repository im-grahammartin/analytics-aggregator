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
            'users': 123,    
        }],
    },{
        'name': 'Test Site 1',
        'results': [{
            'users': 400,    
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
            'users': 123,
            'pageViews': 9435,
        }],
    },{
        'name': 'Test Site 1',
        'results': [{
            'users': 400,    
            'pageViews': 4525
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
            'pageViews': 9435,
        }],
    },{
        'name': 'Test Site 1',
        'results': [{
            'users': 400,    
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

# Combine two lists with multiple dimensions
