#------------------------------------------------------
#            Handling data: read and write
#------------------------------------------------------
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_spectrum(
        filepath:str
        ):
    """
    Returns DataFrame with columns: 
    "counts", "bin", "measurement_time"
    """
    measurement_time = int(pd.read_csv(filepath, skiprows=1, nrows=1, header=None).iloc[0, 0])

    df = pd.read_csv(
        filepath, 
        skiprows=2, 
        header=None, 
        names=['counts']
        )
    df['measurement_time']= measurement_time
    df['bin'] = range(len(df))
    return df

def load_all_spectra(directory):
    """
    Loads all .TKA files in folder. Returns a single data Frame

    ### example: get one specific measurement
    df_90 = df_all[df_all['filename'] == '04-14-01-NaI-90.TKA']

    """
    frames = []
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".TKA"):
            filepath = os.path.join(directory, filename)

            df = load_spectrum(filepath)
            df['filename'] = filename  # tag data with filename

            frames.append(df)
    return  pd.concat(frames, ignore_index=True)



def load_coincidence(
        filepath:str
):
    """
    Returns the data of coincidence measurement.
    name: 'delay', 'coincidences'
    """
    df = pd.read_csv(filepath, 
                     sep=',',
                     names=['delay', 'coincidences']
                    )
    return df



if __name__ == '__main__' and False:
    test_data_path = "../data/test_data/1-co-wed-LA5.TKA"
    test_data = load_spectrum(test_data_path)
    print(test_data)
    channels =np.arange(len(test_data.index))
    counts = test_data['counts'].to_numpy()
    plt.plot(channels[200:], counts[200:])
    plt.savefig("../figures/test_data_plot.png")