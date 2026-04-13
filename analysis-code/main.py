from plotting import interactive_plot
from fitting import set_window
from utils import keep_log, read_entry, read_folder, open_log, post_log
from handling_data import load_spectrum, graph_of_spectrum
import func 


#--------------------------------------------------
#           Here the Analysis shall be performed
#--------------------------------------------------


### select which part of the analysis shall be performed

run_test_ana = True 


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