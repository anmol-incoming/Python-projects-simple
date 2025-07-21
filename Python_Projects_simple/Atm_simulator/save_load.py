import json
import os 

def save_load(user_dict, filename="users.json"):
    with open(filename ,"w") as f:
        json.dump(user_dict,f,indent=4)


def load_user_data(filename='users.json'):
    if os.path.exists(filename):
        with open(filename ,'r') as f:
            return json.load(f)
    else:
        return {}

