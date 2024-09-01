import json
import os

from datetime import datetime
from helpers.save_results import save_results

def test_save_results():
    # Arrange - set up input and expected output
    results = {
        'web|United Kingdom': {
            'users': 700
        },
        'web|United States': {
            'users': 100
        }
    }

    current_date = datetime.today().strftime('%d-%m-%Y')
    file_name = "exports/analytics-aggregator-" + current_date + ".json"

    # Act
    save_results(results)

    # Assert
    with open(file_name, 'r') as file:
        saved_data = json.load(file)

    assert type(saved_data) == dict
    assert len(saved_data) == 2
    assert saved_data == results

    os.remove(file_name)

def test_save_results_custom_name():
    # Arrange - set up input and expected output
    results = {
        'web|United Kingdom': {
            'users': 200
        },
        'web|Japan': {
            'users': 300
        }
    }

    file_name = "test-file-name"

    # Act
    save_results(results, "test-file-name")

    # Assert
    with open("exports/" + file_name + ".json", 'r') as file:
        saved_data = json.load(file)

    assert type(saved_data) == dict
    assert len(saved_data) == 2
    assert saved_data == results

    os.remove("exports/" + file_name + ".json")