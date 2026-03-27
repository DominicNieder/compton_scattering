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



if __name__ == "__main__":
    results_dir = "../results"
    test_target = "test result" 
    test_mu, test_dmu = (6, 0.5) 
    test_result = f"mu={test_mu:.1f}+-{test_dmu:.1f}keV"
    keep_log(results_dir, test_target, test_result)
    