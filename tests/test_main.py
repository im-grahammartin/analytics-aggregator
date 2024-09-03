from main import main
from unittest.mock import patch

@patch('main.get_ga_properties')
@patch('main.generate_ga_report')
@patch('main.aggregate_reports')
@patch('main.save_results')
def test_main(mock_save, mock_aggregate, mock_generate_report, mock_get_ga_propertiers):
        # Arrange - set up input and expected output
        mock_get_ga_propertiers.return_value = [{ 
            'name': 'site_1',
            'property_id': '123'
        }]
        mock_args_return = {
            'metrics': 'metric',
            'dimensions': 'dimension',
            'start_date': 'start',
            'end_date': 'end',
            'avoid_aggregate': True,
        }
        with patch('main.get_arguments', return_value=mock_args_return) as mock_get_args:

            # Act
            main()

            # Assert
            mock_get_args.assert_called_once()
            mock_get_ga_propertiers.assert_called_once()
            mock_generate_report.assert_called_once()
            mock_aggregate.assert_not_called()
            mock_save.assert_called_once()

@patch('main.get_ga_properties')
@patch('main.generate_ga_report')
@patch('main.aggregate_reports')
@patch('main.save_results')
def test_main_multiple_sites(mock_save, mock_aggregate, mock_generate_report, mock_get_ga_propertiers):
        # Arrange - set up input and expected output
        mock_get_ga_propertiers.return_value = [{
            'name': 'site_1',
            'property_id': '123'
        },{
            'name': 'site_2',
            'property_id': '456'
        }]
        mock_args_return = {
            'metrics': 'metric',
            'dimensions': 'dimension',
            'start_date': 'start',
            'end_date': 'end',
            'avoid_aggregate': True,
        }
        with patch('main.get_arguments', return_value=mock_args_return) as mock_get_args:

            # Act
            main()

            # Assert
            mock_get_args.assert_called_once()
            mock_get_ga_propertiers.assert_called_once()
            assert mock_generate_report.call_count == 2
            mock_aggregate.assert_not_called()
            mock_save.assert_called_once()

@patch('main.get_ga_properties')
@patch('main.generate_ga_report')
@patch('main.aggregate_reports')
@patch('main.save_results')
def test_main_multiple_sites_and_aggregate(mock_save, mock_aggregate, mock_generate_report, mock_get_ga_propertiers):
        # Arrange - set up input and expected output
        mock_get_ga_propertiers.return_value = [{
            'name': 'site_1',
            'property_id': '123'
        },{
            'name': 'site_2',
            'property_id': '456'
        }]
        mock_args_return = {
            'metrics': 'metric',
            'dimensions': 'dimension',
            'start_date': 'start',
            'end_date': 'end',
            'avoid_aggregate': False,
        }
        with patch('main.get_arguments', return_value=mock_args_return) as mock_get_args:

            # Act
            main()

            # Assert
            mock_get_args.assert_called_once()
            mock_get_ga_propertiers.assert_called_once()
            assert mock_generate_report.call_count == 2
            mock_aggregate.assert_called_once()
            mock_save.assert_called_once()