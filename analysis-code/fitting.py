#------------------------------------------------------
#           funtion code for finding peaks
#------------------------------------------------------
import numpy as np
from scipy.optimize import curve_fit
from func import gaussian

def fit_gaussian(x, y, p0=None):
    """
    Fits a Gaussian to the data (x, y).
    ---
    x:      array of x values (e.g. channel or energy)
    y:      array of y values (e.g. counts)
    p0:     initial guess [amplitude, center, sigma]
            if None, estimated automatically from data
    ---
    returns: popt, perr
        popt = [amplitude, center, sigma]  (best fit values)
        perr = [d_amplitude, d_center, d_sigma]  (1-sigma uncertainties)
    """
    if p0 is None:
        p0 = [np.max(y), x[np.argmax(y)], np.std(x) / 4]

    popt, pcov = curve_fit(gaussian, x, y, p0=p0)
    perr = np.sqrt(np.diag(pcov))
    return popt, perr


def set_window():
    """

    """