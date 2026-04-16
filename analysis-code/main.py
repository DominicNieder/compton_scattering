from plotting import interactive_plot, plot_coincidence_delay, interactive_spectra, init_plot, add_dataScatter

from fitting import fit_gaussian
from utils import keep_log, read_entry, read_folder, open_log, post_log

from handling_data import load_spectrum, load_all_spectra, load_coincidence

import func 
import os

#--------------------------------------------------
#           Here the Analysis shall be performed
#--------------------------------------------------


### select which part of the analysis shall be performed

run_test_ana       =    False
run_osci           =    False
run_coincidence    =    False
run_spec_calibration =  False 
run_compton =           True




# all directories       
dir_data = "../data"
dir_figures = "../figures"
dir_pictures = "../pictures"
dir_results = "../results"


def test_ana():
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


def osci():
    data_dir_osci = "../data/cali_spectra"



def coincidence():
    """
    Here is the code for the coincidence optimization 
    """
    filename= "../data/coincidence/14-04-01.csv"
    coinci_measure= load_coincidence(filename)
    x_delay= coinci_measure['delay'].to_numpy()
    y_coinci = coinci_measure['coincidences'].to_numpy()
    plot_coincidence_delay(x_delay, y_coinci)



def calibration():
    """
    Here is the code to analyse and do the calibration measurements
    """
    section_cali = "cali_spectra"
    dir_cali= os.path.join(dir_data, section_cali)
    # data frames, selecting data
    df_cali = load_all_spectra(dir_cali,section_cali)
    # by scintillator
    df_cali_plastic= df_cali[df_cali["scintillator"]=="Plastic"]
    df_cali_NaI= df_cali[df_cali["scintillator"]=="NaI(Ti)"]

    # selecting cali spectra 
    cali_spec_1_plastic = df_cali_plastic[df_cali_plastic["date, time"]=="2026-04-15 9:40"].numpy()
    cali_spec_1_NaI = df_cali_NaI[df_cali_NaI["date, time"]=="2026-04-15 9:40"].numpy()
    
 
def compton():
    """
    # Compton Analysis
    - look at all spectra in interactive plot
    """
    
    # data directory
    data_loc = "../data/compton_spectra/"
    data_section = "compton_spectra"
    # here is the data frame cotaining the data
    df = load_all_spectra(data_loc, data_section)

    



# execution:
if run_test_ana:
    test_ana() 

if run_osci:
    osci()

if run_osci:
    coincidence()

if run_spec_calibration:
    calibration()

if run_compton:
    compton()