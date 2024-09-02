# Analytics Aggregator

This tool allows you to gather user analytics data from Google Analytics 4 from multiple properties into a single report. Results can either display each property independently, for example to allow to comparisons across different sites, or aggregated together into a single set, for example to report on the total number of page views across all properties.

## Background

This project uses the [Google Analytics Data API](https://developers.google.com/analytics/devguides/reporting/data/v1) to pull data from multiple Google Analytics properties, that are defined in `/src/data/ga-properties.csv`.

The data is then cleaned, transformed and optionally aggregated before being saved as a JSON export in `/exports`.

_Note that this project is using a Beta API from Google, and may therefore be subject to unannounced breaking changes that require this system to be updated._

## Prerequisites 

- Python >3.10
- Google Cloud Platform Service Account

## Authentication Setup

This service must use a Google Analytics account with the relevant "Viewer" permissions for each property in order to connect to the Google Analytics Data API.

See [API Quickstart](https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries) for the full instructions for how to complete this.

1. Create a service account on Google Cloud Platform
2. Download the `credientials.json` file
3. Assign the service account "Viewer" permissions on all applicable Google Analytics 4 properties
4. Set an environment variable `GOOGLE_APPLICATION_CREDENTIALS` with a path to your `credentials.json` file (e.g. ` export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"`)

## Quick Start

1. Clone this repository to your local system
2. _(Optional)_ Create a virtual environment using `python -m venv analytics-aggregator`, starting it with `source/analytics-aggregator/bin/activate`
3. Run `pip install -r requirements.txt` to install project dependencies
4. Run `python src/main.py --help` to validate the installation and see CLI options

## CLI Options

| Option | Description | Required | Default |
| ---------------- | ---------------- | ---------------- | ---------------- |
| `-h`, `--help` | Shows available options | No | |
| `-m`, `--Metrics` | Metrics that should be included in this report. See [Metrics](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#metrics) for the full list of available metrics. Mutple metrics can be included in a single report by passing them in a comma-separated string e.g. `screenPageViews,activeUsers` | Yes | |
| `-d`, `--Dimensions` | Dimensions to be used to segment the metrics in this report by, for example `platform` will break the results down based on web, iOS and Android platforms. See [Dimensions](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema#dimensions) for the full list of available options. Multiple dimensions may be passed as a comma-separated string e.g. `platorm,country`. | No | `None` |
| `-start`, `--StartDate` | Start date for the report, using either an absolute or relative figure as per [DateRange](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/DateRange)| Yes | |
| `-end`, `--EndDate` | End date for the report, using either an absolute or relative figure as per [DateRange](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1beta/DateRange) | No | `"today"` |
| `-raw`, `--Raw` | Should the report return without aggregation? | No | `True` |


## Tests

Unit tests for this application are within `/tests` using [pytest](https://docs.pytest.org/en/stable/).

Run `pytest` to execute the tests and view a coverage report.
