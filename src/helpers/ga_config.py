import csv
import os

default_file_path = 'src/data/ga-properties.csv'

def get_ga_properties(filepath):
    with open(filepath, 'r') as file:
        data_reader = csv.reader(file)
        data = [row for row in data_reader]
    return data