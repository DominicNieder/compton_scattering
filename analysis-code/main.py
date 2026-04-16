from plotting import interactive_plot, coincidence_delay, interactive_spectra

from fitting import fit_gaussian
from utils import keep_log, read_entry, read_folder, open_log, post_log

from handling_data import load_spectrum, load_all_spectra, load_coincidence

import func 
import os

#--------------------------------------------------
#           Here the Analysis shall be performed
#--------------------------------------------------


### select which part of the analysis shall be performed

run_test_ana = False 
run_osci = False
run_coincidence = False
run_spec_calibration= True



# all directories       
dir_data = "../data"
dir_figures = "../figures"
dir_pictures = "../pictures"
dir_results = "../results"


if run_test_ana:
    test_name = "test_figure"
    description = "This plot will help verify the energy windows."


    data_path = "../data/test_data/1-co-wed-LA5.TKA"
    df_testData = load_spectrum(data_path)
    x, y = graph_of_spectrum(df_testData)
    interactive_plot(test_name, description,x[200:],y[200:])  # open in irefox
    read_entry(dir_figures, test_name) # gives entry to the figure

    entry = open_log(dir_figures) # change
    entry.setdefault('test_data', {}).setdefault('window2', {})
    entry['test_data']['window1']['1'] = 5888
    entry['test_data']['window1']['2'] = 6100
    post_log(dir_figures, entry)
    read_folder(dir_figures)


if run_osci:
    data_dir_osci = "../data/cali_spectra"


"""
Here is the code for the coincidence optimization 
"""
if run_coincidence:
    filename= "../data/coincidence/14-04-01.csv"
    coinci_measure= load_coincidence(filename)
    x_delay= coinci_measure['delay'].to_numpy()
    y_coinci = coinci_measure['coincidences'].to_numpy()
    coincidence_delay(x_delay, y_coinci)


"""
Here is the code to analyse and do the calibration measurements
"""
if run_spec_calibration:
    section_cali = "cali_spectra"
    dir_cali= os.path.join(dir_data, section_cali)
    # data frames, selecting data
    df_cali = load_all_spectra(dir_cali,section_cali)

    df_cali_plastic= df_cali[df_cali["scintillator"]=="Plastic"]
    df_cali_NaI= df_cali[df_cali["scintillator"]=="NaI(Ti)"]
    # names and log entries
    name_plastic = "cali_plastic_scinti"
    name_NaI = "cali_NaI_scinti"
    log_plastic= "compare the calibration spectra, select windows, focus on data obtained on 04-15"
    log_NaI= "compare the calibration spectra, select windows, focus on data obtained on 04-15"
    # interactive plot
    interactive_spectra(
        df_cali_plastic, 
        name_plastic, 
        log_plastic, 
        label_col="time_of_recording"
        )
    interactive_spectra(
        df_cali_NaI,
        name_NaI,
        log_NaI,
        label_col="time_of_recording"
    )
    
