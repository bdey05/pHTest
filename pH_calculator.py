import json
import numpy as np
import math

def alpha():
    try:
        with open('all_TPEN_DERIVATIVE_records.json', 'r', encoding = 'utf-8') as f:
    #the load function will directly load and parse the file, creating a dictionary 
            json_data = json.load(f)

            filtered_data = []

            for aqueous in json_data["aqueous phase"]:
                aqueous_data = {
                "solutes" == aqueous["solutes"],
                "pH" == aqueous["pH"],
                "volume" == aqueous["volume"],}
                            
            filtered_data.append(aqueous_data)
                        
            if isinstance("pH", (int, float)):
                pH = np.array("pH", dtype=float)
                            
                h3o = -math.log10(pH)
                return h3o
            else:
                return None
            
    except ValueError:
        print('Decoding JSON has failed')

    print(h3o)

    alpha()
