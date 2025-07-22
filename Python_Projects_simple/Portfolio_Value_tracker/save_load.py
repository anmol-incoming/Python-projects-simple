import json
import os 
def save_load(all_users,filename="all_users.json"):
    with open(filename,"w") as f:
        json.dump(all_users,f,indent=4)

def load_user_data(filename='all_users.json'):
    if os.path.exists(filename):
        with open(filename,'r') as f:
            return json.load(f)
    else:
        return {}




