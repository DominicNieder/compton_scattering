#--------------------------------------------------
#            Models shall be performed
#--------------------------------------------------
import numpy as np


def gaussian(x, A, mu, sigma):
    """
    Gaussian function: 
    g(x)=A * e^{-(x-mu)^2 / (2*sigma^2)} 

    """
    return A * np.exp(-(x-mu)**2 / (2*sigma**2))