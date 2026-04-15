#------------------------------------------------------
#            Handling data: read and write
#------------------------------------------------------
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils import return_scinti, return_TOR, return_angle

def load_spectrum(filepath):
    """
    Returns DataFrame with columns: 
    "counts", "bin", "measurement_time"
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    # obtain measurement time - considere inclusion of condition based on plastic- or NaI-scintillator
    measurement_time = int(pd.read_csv(filepath, skiprows=1, nrows=1, header=None).iloc[0, 0])
    # create dataframe
    df = pd.read_csv(filepath, skiprows=2, header=None, names=['counts'])
    l =len(df)
    # add bin number
    df['bin'] = range(l)
    # add measurement time
    df['measurement_time']= measurement_time    
    if df.empty:
        print(f"Warning: {filepath} loaded but is empty")
    else:
        print(f"Loaded {filepath} — {len(df)} bins")
    
    return df


def load_all_spectra(directory, section=None):
    """
    Loads all .TKA files in directory. Returns a single data Frame

    ### keys:
    'counts', 'bin', 'measurement_time'
    'angle', 'scintillator', 'time_of_recording', filename

    ### example: get one specific measurement
    df_90 = df_all[df_all['filename'] == '04-14-01-NaI-90.TKA']
    """    
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")

    files = [f for f in sorted(os.listdir(directory)) if f.endswith(".TKA")]
    
    ### checking number of 
    if not files:
        print(f"Warning: no .TKA files found in {directory}")
        return pd.DataFrame()

    print(f"Found {len(files)} .TKA files in {directory}")
    frames = []

    for filename in files:
        print(f"{filename}")
        filepath = os.path.join(directory, filename)
        df = load_spectrum(filepath)
        print(f"dir: {directory}")
        df['angle'] = return_angle(section, filename)
        df['scintillator'] = return_scinti(section, filename)
        df['time_of_recording']= return_TOR(section, filename)
        df['filename'] = filename  # tag data with filename
        frames.append(df)
        print(f"{len(df)} bins, N={np.sum(df['counts'])}, time of recording={df['time_of_recording'][0]}" )
    df_all = pd.concat(frames, ignore_index=True)

    print(f"Combined DataFrame: {len(df_all)} rows, {df_all['filename'].nunique()} files")

    return df_all

# def load_spectrum(
#         filepath:str
#         ):
#     """
#     Returns DataFrame with columns: 
#     "counts", "bin", "measurement_time"
#     """
#     measurement_time = int(pd.read_csv(filepath, skiprows=1, nrows=1, header=None).iloc[0, 0])

#     df = pd.read_csv(
#         filepath, 
#         skiprows=2, 
#         header=None, 
#         names=['counts']
#         )
#     l =len(df)
#     df['bin'] = range(l)
#     df['measurement_time']= measurement_time

#     return df

# def load_all_spectra(directory):
#     """
#     Loads all .TKA files in directory. Returns a single data Frame

#     ### keys:
#     'counts', 'bin', 'measurement_time'
#     'angle', 'scintillator', 'time_of_recording', filename

#     ### example: get one specific measurement
#     df_90 = df_all[df_all['filename'] == '04-14-01-NaI-90.TKA']
#     """
#     frames = []
#     for filename in sorted(os.listdir(directory)):
#         if filename.endswith(".TKA"):
#             filepath = os.path.join(directory, filename)

#             df = load_spectrum(filepath)
#             df['angle'] = return_angle(directory, filename)
#             df['scintillator'] = return_scinti(directory, filename)
#             df['time_of_recording']= return_TOR(directory, filename)
#             df['filename'] = filename  # tag data with filename
#             frames.append(df)
#     return  pd.concat(frames, ignore_index=True)



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