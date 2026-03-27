#------------------------------------------------------
#            Handling data: read and write
#------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_spectrum(filepath):
    """
    Returns DataFrame with columns: counts
    """
    df = pd.read_csv(filepath, sep='/t', comment='#',
                     names=['counts'])
    return df





if __name__ == '__main__':
    test_data_path = "../data/test_data/1-co-wed-LA5.TKA"
    test_data = load_spectrum(test_data_path)
    print(test_data)
    channels =np.arange(len(test_data.index))
    counts = test_data['counts'].to_numpy()
    plt.plot(channels[200:], counts[200:])
    plt.savefig("../figures/test_data_plot.png")