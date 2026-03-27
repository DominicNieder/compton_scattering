#------------------------------------------------------
#            utilities: i.e. editing .json files
#------------------------------------------------------

import os 
import json
from datetime import datetime


def log_file(folder, filename, description):
    """
    Add or update an entry in orientation.json
    ---
    folder:         the target folder of object
    filename:       the target filename to be described
    description:    the suitable description of filename
    """
    log_path = os.path.join(folder, "orientation.json")

    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            index = json.load(f)
    else:
        index = {}
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    index[filename] = {
                        "description": description,
                        "update": timestamp
                    }
    
    with open(log_path, "w") as f:
        json.dump(index, f, indent=2)