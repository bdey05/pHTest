import json
import numpy as np
import math 

def alpha(file_name):

    with open(file_name, "r",  encoding = 'utf-8') as file:
    
        json_data = json.load(file)
    
    filtered_data = []
    
    if (isinstance(json_data, list)):
        for record in json_data:
            #print(record['aqueous phase']['solutes'])
            filtered_data.append(record["aqueous phase"])

    if (isinstance(json_data, dict)):
        #print(json_data["aqueous phase"])
        filtered_data.append(json_data["aqueous phase"])

    for record in filtered_data:
        if (isinstance(record['pH'], int)):
            print("pH is present and valid")
        else:
            print("pH is not int. Here are the solutes:", record['solutes'])


alpha("all_TPEN_DERIVATIVE_records.json")