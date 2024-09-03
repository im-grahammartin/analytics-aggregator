import csv
import os

def get_ga_properties(filepath = 'src/data/ga-properties.csv'):
    with open(filepath, 'r') as file:
        data_reader = csv.DictReader(file)
        data = [row for row in data_reader]
    return data