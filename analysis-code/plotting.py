#------------------------------------------------------
#       plotting: functions for quick plotting 
#------------------------------------------------------
import pandas as pd
import numpy as np
from utils import keep_log
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import os

STYLE = {
    "figure.dpi":      150,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid":       True,
    "grid.alpha":      0.3,

    "lines.linewidth":    1.5,
    "lines.markersize":   4,
    # "errorbar.capsize":   3,


    "axes.prop_cycle": plt.cycler(color=[
        "#e34a33", 
        "#3182bd",
        "#31a354", 
        "#5a07c0"
        ]),
    
    "font.size":       11,
    "text.usetex":      True,
    "font.family":      "serif"
}

def init_plot(x_label: str, y_label: str, nrows: int = 1, ncols: int = 1, size: tuple = (6, 4)):
    """
    Creates a styled figure with one or more subplots.
    Returns (fig, axes) — axes is a single Axes if nrows==ncols==1,
    otherwise a numpy array of Axes, matching plt.subplots behaviour.
    ---
    x_label:  x-axis label (applied to all subplots)
    y_label:  y-axis label (applied to all subplots)
    nrows:    number of subplot rows
    ncols:    number of subplot columns
    size:     figure size in inches (width, height)
    """
    with plt.rc_context(STYLE):
        fig, axes = plt.subplots(nrows, ncols, figsize=size, tight_layout=True)

    ax_flat = [axes] if nrows == ncols == 1 else axes.flat
    for ax in ax_flat:
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)

    return fig, axes


def add_dataScatter(ax, x, y, error, label: str = None, colour: str = None):
    """
    Adds a data graph with error bars to an existing axes.
    The error band is drawn as a shaded region with low opacity.
    ---
    ax:     matplotlib Axes object
    x:      x data (array-like)
    y:      y data (array-like)
    error:  y uncertainties (array-like), same length as y
    colour: line and band colour (e.g. 'tab:blue' or '#e34a33')
    label:  legend label (optional)
    """
    marker_size = 5
    lines = ax.plot(
        x, 
        y,
        color=colour, 
        # markerfacecolor='white',
        marker='s', 
        markersize=marker_size,
        linestyle='none', 
        label=label, 
        zorder=2
    )
    ax.vlines(
        x, 
        y - error, 
        y + error,
        color=lines[0].get_color(), 
        alpha=0.4, 
        linewidth=marker_size - 1,
        zorder=1
    )


    return ax

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


def plot_coincidence_delay(
        x_delay_times,
        y_coincidences
):
    """
    plots the data acquired by the coincidence measurement.
    """
    directory= "../figures"
    file_name= "coincidences.png"
    description= "This graph shows that the delay time can be varied in between 1.6-2.4 micro sec. The Linear gate seems to function like a plateau: coincidence / no coincidence. We chose to set the delay to 2.12 micro sec."

    save_file = os.path.join(directory,file_name)
    fig, ax = init_plot(
        x_label=r"delay time ($\mu$s)",
        y_label="coincidences"
    )
    add_dataScatter(
        ax,
        x=x_delay_times,
        y=y_coincidences,
        error=np.sqrt(y_coincidences),
        label= "coincidences"
    )
    with plt.rc_context(STYLE):
        fig.savefig(save_file)
    keep_log(directory, file_name, description)



def interactive_spectra(df, name, description, x_col='bin', label_col='filename'):
    """
    Plots all spectra in a combined DataFrame as separate traces.
    Each trace can be toggled on/off interactively.
    ---
    df:         combined DataFrame from load_all_spectra
    name:       output filename (no extension)
    description: log entry
    x_col:      column to use as x-axis (e.g. 'bin' or 'energy')
    label_col:  column used to label each trace (e.g. 'filename' or 'angle')
    """
    directory = "../figures"
    save_file = os.path.join(directory, f"{name}.html")

    fig = go.Figure()

    for label, group in df.groupby(label_col):
        trace_name = " | ".join(str(l) for l in label) if isinstance(label, tuple) else str(label)
        fig.add_trace(go.Scatter(
            x=group[x_col].to_numpy(),
            y=group['counts'].to_numpy(),
            mode='lines',
            name=trace_name
        ))

    fig.update_layout(
        xaxis_title=x_col,
        yaxis_title="Counts",
        legend=dict(itemclick="toggle", itemdoubleclick="toggleothers")
    )

    fig.write_html(save_file)
    keep_log(directory, name, description)


def interactive_calibration(calibration_dataframe):
    """
    This function plots .html, spectra of calibration data.

    Insentive is to find winodows for find gaussian fit parameters thus calibration data. 
    """
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


if __name__ == "__name__" and True:
    test_name = "test_data"
    description = "This plot will help verify the energy windows."

    interactive_plot()