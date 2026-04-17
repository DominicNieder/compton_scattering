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


def return_scinti(data_dir, filename):
    """
    # Which scintilator?
    returns the scintilator used for the file (data_dir/filename)
    data_dir : index key
    filename : index key of data_dir
    """
    directory= "../data"
    index= open_log(directory)
    return index.get(data_dir, {}).get(filename, {}).get("scinti", "unknown")


def return_TOR(data_dir, filename):
    """
    # Time of recording
    returns the date, time
    data_dir : index key
    filename : index key of data_dir
    """
    directory= "../data"
    index= open_log(directory)
    print(index[data_dir][filename])
    return index.get(data_dir, {}).get(filename, {}).get("date, time", "unknown")

def return_angle(data_dir, filename):
    """
    # measurement angle 
    returns the angle
    data_dir : index key
    filename : index key of data_dir
    """
    directory= "../data"
    index= open_log(directory)
    return index.get(data_dir, {}).get(filename, {}).get("angle", "unknown")

def return_source(data_dir, filename):
    """
    # measured spectra of which source?
    """
    directory= "../data"
    index= open_log(directory)
    return index.get(data_dir, {}).get(filename, {}).get("source", "unknown")


if __name__ == "__main__" and True:
    print(return_TOR("cali_spectra", "04-15-01-Na-NaI.TKA"))
