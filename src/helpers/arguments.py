import argparse

def get_arguments():
    parser = argparse.ArgumentParser(
        prog="Analytics Aggregator",
        description="CLI tool to aggregate data from Google Analytics 4 prpoerties",
        epilog="See full dimension and metric options here https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema and https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/DateRange for date options",
    )

    parser.add_argument("-m", "--Metrics", help = "Comma separated list of Google Analyitcs metrics to include", required=True)
    parser.add_argument("-d", "--Dimensions", help = "Comma separated list of Google Analytics dimensions", default=None)
    parser.add_argument("-start", "--StartDate", help = "Start date for report data", required=True)
    parser.add_argument("-end", "--EndDate", help = "End date for report, defaults to today", default="tody")
    parser.add_argument("-raw", "--Raw", help = "Return data without aggregation?", action="store_true")

    args = parser.parse_args()

    return {
        'metrics': args.Metrics,
        'dimensions': args.Dimensions,
        'start_date': args.StartDate,
        'end_date': args.EndDate,
        'avoid_aggregate': args.Raw,
    }