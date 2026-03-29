#------------------------------------------------------
#       plotting: functions for quick plotting 
#------------------------------------------------------

from utils import keep_log
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import os


def plot_spectrum(
        name: str,
        description: str, 
        x_data, 
        y_data
        ):
    """
    A simple example plot.
    Saves figure of a given data. Creats log entry. 
    
    name: File name. No ending like .pdf, .png, ...
    description: comes to the log file
    x_data: data
    y_data: data
    """
    directory = "../figures"
    file_name = f"{name}.png"
    save_file = os.path.join(directory,file_name)
    plt.plot(x_data, y_data)
    plt.ylabel("Counts")
    plt.xlabel("Channels/bins")
    plt.savefig(save_file)
    # keeping log of the figure w
    keep_log(directory, name, description)


def interactive_plot(
        name:str, 
        description:str, 
        x_data, 
        y_data, 
        error=None
        ):
    """
    Creats an interactive plot. Allows for quick Selectoion of i.e. windows. 
    """
    directory = "../figures"
    file_name= f"{name}.html"
    save_file = os.path.join(directory,file_name)

    fig = go.Figure()
    if error==None:
        fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='markers'))
    else:
        fig.add_trace(go.Scatter(
            x=x_data,
            y=y_data,
            error_y=dict(array=error)
        ))
    fig.write_html(save_file)    # interactive
    keep_log(directory, name, description)


if __name__ == "__name__" and True:
    test_name = "test_data"
    description = "This plot will help verify the energy windows."

    interactive_plot()