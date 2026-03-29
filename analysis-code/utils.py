#------------------------------------------------------
#            utilities: i.e. editing .json files
#------------------------------------------------------

import os 
import json
from datetime import datetime


def keep_log(folder, target, description):
    """
    Add or update an entry in orientation.json;
    The entry type is 'dict';
    ---
    folder:         the target folder of object
    target:       the target filename to be described
    description:    the suitable description of filename
    """
    log_path = os.path.join(folder, "orientation.json")

    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            index = json.load(f)
    else:
        index = {}
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    index[target] = {
                        "description": description,
                        "update": timestamp
                    }
    
    with open(log_path, "w") as f:
        json.dump(index, f, indent=2)


def describe_data(data_name, data_description):
    """
    Keep log on the data taken.

    description: short description of data
    """
    log_path = os.path.join("../data", "orientation.json")
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            index = json.load(f)
    else:
        index = {}
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    index[data_name] = {
                        "description": data_description,
                        "update": timestamp
                    }

    with open(log_path, "w") as f:
        json.dump(index, f, indent=2)


def read_folder(folder):
    """
    Prints all entries in orientation.json of the given folder.
    """
    log_path = os.path.join(folder, "orientation.json")
    with open(log_path, "r") as f:
        index = json.load(f)

    for filename, entry in sorted(index.items()):
        print(f"{filename} ({entry['update']}):\n{entry['description']}\n")



def read_entry(folder, target):
    """
    prints the entry of the target.
    """
    log_path = os.path.join(folder, "orientation.json")
    with open(log_path, "r") as f:
        index = json.load(f)
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