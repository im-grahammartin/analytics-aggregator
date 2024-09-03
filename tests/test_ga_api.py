from unittest.mock import patch, call, Mock
from api.ga import build_metrics, build_dimensions, build_report_request, generate_ga_report, clean_ga_response


def test_build_metrics_single():
    with patch('api.ga.Metric', return_value='test') as mock_metrics:
        # Arrange - set up input and expected output
        expected_type = list
        expected_length = 1 
        expected_response = ['test']

        # Act
        metrics = build_metrics('one')

        # Assert
        assert type(metrics) == expected_type
        assert len(metrics) == expected_length
        assert metrics == expected_response
        mock_metrics.assert_called_once()
        mock_metrics.assert_called_once_with(name='one')

def test_build_metrics_multiple():
    with patch('api.ga.Metric', return_value='test') as mock_metrics:
        # Arrange - set up input and expected output
        expected_type = list
        expected_length = 2 
        expected_response = ['test','test']

        # Act
        metrics = build_metrics('one,two')

        # Assert
        assert type(metrics) == expected_type
        assert len(metrics) == expected_length
        assert metrics == expected_response
        mock_metrics.assert_called()
        assert mock_metrics.call_count == expected_length
        mock_metrics.assert_has_calls([call(name='one'), call(name='two')])

def test_build_metrics_multiple_with_whitespace():
    with patch('api.ga.Metric', return_value='test') as mock_metrics:
        # Arrange - set up input and expected output
        expected_type = list
        expected_length = 2 
        expected_response = ['test','test']

        # Act
        metrics = build_metrics('one, two')

        # Assert
        assert type(metrics) == expected_type
        assert len(metrics) == expected_length
        assert metrics == expected_response
        mock_metrics.assert_called()
        assert mock_metrics.call_count == expected_length
        mock_metrics.assert_has_calls([call(name='one'), call(name='two')])

def test_build_dimensions_single():
    with patch('api.ga.Dimension', return_value='test') as mock_dimensions:
        # Arrange - set up input and expected output
        expected_type = list
        expected_length = 1 
        expected_response = ['test']

        # Act
        dimensions = build_dimensions('one')

        # Assert
        assert type(dimensions) == expected_type
        assert len(dimensions) == expected_length
        assert dimensions == expected_response
        mock_dimensions.assert_called_once()
        mock_dimensions.assert_called_once_with(name='one')

def test_build_dimensions_multiple():
    with patch('api.ga.Dimension', return_value='test') as mock_dimensions:
        # Arrange - set up input and expected output
        expected_type = list
        expected_length = 2 
        expected_response = ['test','test']

        # Act
        dimensions = build_dimensions('one,two')

        # Assert
        assert type(dimensions) == expected_type
        assert len(dimensions) == expected_length
        assert dimensions == expected_response
        mock_dimensions.assert_called()
        assert mock_dimensions.call_count == expected_length
        mock_dimensions.assert_has_calls([call(name='one'), call(name='two')])

def test_build_dimensions_multiple_with_whitespace():
    with patch('api.ga.Dimension', return_value='test') as mock_dimensions:
        # Arrange - set up input and expected output
        expected_type = list
        expected_length = 2 
        expected_response = ['test','test']

        # Act
        dimensions = build_dimensions('one, two')

        # Assert
        assert type(dimensions) == expected_type
        assert len(dimensions) == expected_length
        assert dimensions == expected_response
        mock_dimensions.assert_called()
        assert mock_dimensions.call_count == expected_length
        mock_dimensions.assert_has_calls([call(name='one'), call(name='two')])

def test_build_report_request():
    with patch('api.ga.RunReportRequest', return_value=True) as mock_report_request:
        with patch('api.ga.Metric', return_value='test-metric'):
            with patch('api.ga.DateRange', return_value='test-dates'):
                # Arrange - set up input and expected output
                expected_type = bool
                expected_response = True
                expected_call = call(
                        property='properties/123456',
                        metrics=['test-metric'],
                        dimensions=[],
                        date_ranges=['test-dates']
                    )
                
                # Act
                report = build_report_request(
                    property_id='123456',
                    start_date='10daysAgo',
                    end_date='yesterday',
                    metrics_str='screenPageViews',
                )

                # Assert
                assert type(report) == expected_type
                assert report == expected_response
                mock_report_request.assert_called_once()
                assert mock_report_request.call_args == expected_call

def test_build_report_request_with_dimensions():
    with patch('api.ga.RunReportRequest', return_value=True) as mock_report_request:
        with patch('api.ga.Metric', return_value='test-metric'):
            with patch('api.ga.Dimension', return_value='test-dimension'):
                with patch('api.ga.DateRange', return_value='test-dates'):
                    # Arrange - set up input and expected output
                    expected_type = bool
                    expected_response = True
                    expected_call = call(
                            property='properties/123456',
                            metrics=['test-metric'],
                            dimensions=['test-dimension'],
                            date_ranges=['test-dates']
                        )
                    
                    # Act
                    report = build_report_request(
                        property_id='123456',
                        start_date='10daysAgo',
                        end_date='yesterday',
                        metrics_str='screenPageViews',
                        dimensions_str='platform',
                    )

                    # Assert
                    assert type(report) == expected_type
                    assert report == expected_response
                    mock_report_request.assert_called_once()
                    assert mock_report_request.call_args == expected_call

def test_generate_ga_report():
    with patch('api.ga.BetaAnalyticsDataClient') as mock_beta_analytics_data_client:
        with patch('api.ga.BetaAnalyticsDataClient.run_report') as mock_run_report:
        
            # Arrange - set up input and expected output
            expected_type = list
            expected_length = 0
            expected_response = []
            expected_call = []
            
            # Act
            report = generate_ga_report(
                property_id='123456',
                start_date='10daysAgo',
                end_date='yesterday',
                metrics='screenPageViews',
                dimensions='platform',
            )

            # Assert
            mock_beta_analytics_data_client.assert_called_once()
            mock_beta_analytics_data_client().run_report.assert_called_once()
            assert mock_beta_analytics_data_client.call_args == expected_call
            assert type(report) == expected_type
            assert len(report) == expected_length
            assert report == expected_response

def test_clean_ga_response_with_dimensions():
    # Arrange - set up input and expected output
    expected_type = list
    expected_dimension_length = 1
    expected_dimension_name = 'mock_dimension'
    expected_dimension_value = 'test_dimension_value'
    expected_metric_name = 'mock_metric'
    expected_metric_value = 100
    expected_metric_type = int

    # GA Response is a heavily nested class – mocking each element of this 
    mockResponse = Mock()
    mockRow = Mock()
    mockMetricHeader = Mock()
    mockDimensionHeader = Mock()
    mockMetricValue = Mock()
    mockDimensionValue = Mock()

    mockMetricHeader.name = expected_metric_name
    mockDimensionHeader.name = expected_dimension_name
    mockMetricValue.value = expected_metric_value
    mockDimensionValue.value = expected_dimension_value
    mockRow.dimension_values = [mockDimensionValue]
    mockRow.metric_values = [mockMetricValue]
    mockResponse.dimension_headers = [mockDimensionHeader]
    mockResponse.metric_headers = [mockMetricHeader]
    mockResponse.rows = [mockRow]
    mockResponse.kind = 'mock_kind'
    
    # Act
    cleaned_response = clean_ga_response(mockResponse)

    # Assert
    assert type(cleaned_response) == expected_type
    assert expected_dimension_name in cleaned_response[0]['dimensions']
    assert len(cleaned_response[0]['dimensions']) == expected_dimension_length
    assert cleaned_response[0]['dimensions'][expected_dimension_name] == expected_dimension_value
    assert expected_metric_name in cleaned_response[0]['metrics']
    assert cleaned_response[0]['metrics'][expected_metric_name] == expected_metric_value
    assert type(cleaned_response[0]['metrics'][expected_metric_name]) == expected_metric_type
    assert 'kind' not in cleaned_response[0]

def test_clean_ga_response_with_multiple_dimensions():
    # Arrange - set up input and expected output
    expected_type = list
    expected_dimension_length = 2
    expected_dimension_name = 'mock_dimension'
    expected_dimension_name_2 = 'another_mock_dimension'
    expected_dimension_value = 'test_dimension_value'
    expected_metric_name = 'mock_metric'
    expected_metric_value = 100
    expected_metric_type = int

    # GA Response is a heavily nested class – mocking each element of this 
    mockResponse = Mock()
    mockRow = Mock()
    mockMetricHeader = Mock()
    mockDimensionHeader = Mock()
    mockDimensionHeader2 = Mock()
    mockMetricValue = Mock()
    mockDimensionValue = Mock()

    mockMetricHeader.name = expected_metric_name
    mockDimensionHeader.name = expected_dimension_name
    mockDimensionHeader2.name = expected_dimension_name_2
    mockMetricValue.value = expected_metric_value
    mockDimensionValue.value = expected_dimension_value
    mockRow.dimension_values = [mockDimensionValue, mockDimensionValue]
    mockRow.metric_values = [mockMetricValue]
    mockResponse.dimension_headers = [mockDimensionHeader,mockDimensionHeader2]
    mockResponse.metric_headers = [mockMetricHeader]
    mockResponse.rows = [mockRow]
    mockResponse.kind = 'mock_kind'
    
    # Act
    cleaned_response = clean_ga_response(mockResponse)

    # Assert
    assert type(cleaned_response) == expected_type
    assert expected_dimension_name in cleaned_response[0]['dimensions']
    assert expected_dimension_name_2 in cleaned_response[0]['dimensions']
    assert len(cleaned_response[0]['dimensions']) == expected_dimension_length
    assert cleaned_response[0]['dimensions'][expected_dimension_name] == expected_dimension_value
    assert cleaned_response[0]['dimensions'][expected_dimension_name_2] == expected_dimension_value
    assert expected_metric_name in cleaned_response[0]['metrics']
    assert cleaned_response[0]['metrics'][expected_metric_name] == expected_metric_value
    assert type(cleaned_response[0]['metrics'][expected_metric_name]) == expected_metric_type
    assert 'kind' not in cleaned_response[0]

def test_clean_ga_response_without_dimensions():
    # Arrange - set up input and expected output
    expected_type = list
    expected_dimension_name = 'mock_dimension'
    expected_dimension_value = 'test_dimension_value'
    expected_metric_name = 'mock_metric'
    expected_metric_value = 100
    expected_metric_type = int

    # GA Response is a heavily nested class – mocking each element of this 
    mockResponse = Mock()
    mockRow = Mock()
    mockMetricHeader = Mock()
    mockDimensionHeader = Mock()
    mockMetricValue = Mock()
    mockDimensionValue = Mock()

    mockMetricHeader.name = expected_metric_name
    mockDimensionHeader.name = expected_dimension_name
    mockMetricValue.value = expected_metric_value
    mockDimensionValue.value = expected_dimension_value
    mockRow.metric_values = [mockMetricValue]
    mockResponse.dimension_headers = []
    mockResponse.metric_headers = [mockMetricHeader]
    mockResponse.rows = [mockRow]
    mockResponse.kind = 'mock_kind'
    
    # Act
    cleaned_response = clean_ga_response(mockResponse)

    # Assert
    assert type(cleaned_response) == expected_type
    assert 'dimensions' not in cleaned_response[0]
    assert expected_metric_name in cleaned_response[0]['metrics']
    assert cleaned_response[0]['metrics'][expected_metric_name] == expected_metric_value
    assert type(cleaned_response[0]['metrics'][expected_metric_name]) == expected_metric_type
    assert 'kind' not in cleaned_response[0]

