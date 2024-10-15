import pytest
import os
import csv

from file.ga_config import get_ga_properties

@pytest.fixture(scope='module')
def ga_properties():
    with open('ga-properties.csv', 'w', newline='') as ga_properties:
        fieldnames = ['name', 'property_id']
        ga_file_writer = csv.DictWriter(ga_properties, fieldnames=fieldnames)
        ga_file_writer.writeheader()
        ga_file_writer.writerow({'name' : 'Test GA Property Name', 'property_id' : '123456789'})
    yield
    os.remove('ga-properties.csv')

def test_get_ga_properties(ga_properties):
    # Arrange - set up input and expected output
    expected_length = 1
    expected_name = 'Test GA Property Name'
    expected_id = '123456789'
    expected_type = list

    # Act
    ga_data = get_ga_properties('ga-properties.csv')

    # Assert
    assert type(ga_data) == expected_type
    assert len(ga_data) == expected_length
    assert ga_data[0]['name'] == expected_name
    assert ga_data[0]['property_id'] == expected_id