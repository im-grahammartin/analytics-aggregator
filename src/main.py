import sys

from interface.cli_arguments import get_arguments
from file.ga_config import get_ga_properties
from api.ga import generate_ga_report
from transformers.aggregator import aggregate_reports
from file.save_results import save_results

def main():
    
    # Get CLI arguments
    args = get_arguments()
    metrics, dimensions, start_date, end_date, avoid_aggregate = args.values()

    # Get GA properties from fixed config file
    ga_properties = get_ga_properties()

    combined_reports = []

    for ga_property in ga_properties:
        site_name = ga_property['name']
        print(f'Collecting data for {site_name}')

        # Collect data using GA Data API
        ga_report = generate_ga_report(
            ga_property['property_id'], 
            start_date, 
            end_date, 
            metrics, 
            dimensions
        )

        combined_reports = combined_reports + [{ 'name': ga_property['name'], 'results': ga_report }]

    if(avoid_aggregate):
        save_results(combined_reports)
    else:
        # Aggragate all data into a single report before saving
        aggregated_data = aggregate_reports(combined_reports)
        save_results(aggregated_data)

if __name__ == '__main__':
    sys.exit(main())