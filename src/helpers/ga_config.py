import csv
import os

def get_ga_properties(filepath = 'src/data/ga-properties.csv'):
    with open(filepath, 'r') as file:
        data_reader = csv.DictReader(file)
        # mydict = {rows[0]:rows[1] for rows in data_reader}
        data = [row for row in data_reader]
        # data = []
        # print(mydict)
        print(data)
    return data