import json
import os

from datetime import datetime

dir_name = 'exports'

def save_results(data, file_name=None):
    if(file_name is None):
        current_date = datetime.today().strftime('%d-%m-%Y')
        file_name = "analytics-aggregator-" + current_date
    
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    json_object = json.dumps(data, indent=4)
 
    with open(dir_name + "/" + file_name + ".json", "w") as outfile:
        success = outfile.write(json_object)
    

    
