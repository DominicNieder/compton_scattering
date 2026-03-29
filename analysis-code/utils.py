#------------------------------------------------------
#            utilities: i.e. editing .json files
#------------------------------------------------------

import os 
import json
from datetime import datetime

def open_log(target_folder:str)->dict:
    """
    Opens the json file. Returns Dictionary.
    """
    log_path = os.path.join(target_folder, "orientation.json")
    if not os.path.exists(log_path):
        raise FileNotFoundError(f"No orientation.json found in {target_folder}")

    else:
        with open(log_path, "r") as f:
            index = json.load(f)
            return index


def post_log(target_folder, index):
    """
    post log to json file.
    """
    log_path = os.path.join(target_folder, "orientation.json")
    if not os.path.exists(log_path):
        raise FileNotFoundError(f"No orientation.json found in {target_folder}")
    else:
        with open(log_path, "w") as f:
            json.dump(index, f, indent=2)
    

def keep_log(folder, target, description):
    """
    Add or update an entry in orientation.json;
    The entry type is 'dict';
    ---
    folder:         the target folder of object
    target:       the target filename to be described
    description:    the suitable description of filename
    """
    index = open_log(folder)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    index[target] = {
                        "description": description,
                        "update": timestamp
                    }
    post_log(folder, index)





def describe_data(data_name, data_description):
    """
    Keep log on the data taken.

    description: short description of data
    """
    data_dir = "../data"
    index = open_log(data_dir)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    index[data_name] = {
                        "description": data_description,
                        "Time": timestamp
                    }
    post_log(data_dir, index)


def read_folder(folder):
    index = open_log(folder)
    for filename, entry in sorted(index.items()):
        print(f"{filename}:")
        if isinstance(entry, dict):
            for key, value in entry.items():
                print(f"  {key}: {value}")
        else:
            print(f"  {entry}")
        print()



def read_entry(folder, target):
    """
    Prints the entry of the target.
    """
    index = open_log(folder)
    print("Target: ", target, " recordet at", index[target]["update"])
    print("description: ", index[target]["description"])


if __name__ == "__main__" and False:
    results_dir = "../results"
    test_target = "test result1" 
    test_mu, test_dmu = (6.5, 0.5) 
    test_result = f"mu={test_mu:.1f}+-{test_dmu:.1f}keV\nThis is a very long message because we have alot to say  and there were a couple of details that need to be mentioned and so when we see a slight shift in the continum of space time we can take this too into consideration so that we can all be very happy."
    keep_log(results_dir, test_target, test_result)


if __name__ == "__main__" and False:
    results_dir = "../results"
    test_target = "test result"
    read_folder(results_dir)
    #read_entry(results_dir, test_target)