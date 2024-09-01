from helpers.ga_api import build_metrics, build_dimensions, build_report_request
from unittest.mock import patch, call

def test_build_metrics_single():
    with patch("helpers.ga_api.Metric", return_value='test') as mock_metrics:
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
    with patch("helpers.ga_api.Metric", return_value='test') as mock_metrics:
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
    with patch("helpers.ga_api.Metric", return_value='test') as mock_metrics:
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
    with patch("helpers.ga_api.Dimension", return_value='test') as mock_dimensions:
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
    with patch("helpers.ga_api.Dimension", return_value='test') as mock_dimensions:
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
    with patch("helpers.ga_api.Dimension", return_value='test') as mock_dimensions:
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
    with patch("helpers.ga_api.RunReportRequest", return_value=True) as mock_report_request:
        with patch("helpers.ga_api.Metric", return_value='test-metric'):
            with patch("helpers.ga_api.DateRange", return_value='test-dates'):
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
    with patch("helpers.ga_api.RunReportRequest", return_value=True) as mock_report_request:
        with patch("helpers.ga_api.Metric", return_value='test-metric'):
            with patch("helpers.ga_api.Dimension", return_value='test-dimension'):
                with patch("helpers.ga_api.DateRange", return_value='test-dates'):
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