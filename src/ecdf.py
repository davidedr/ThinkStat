'''
Created on 04 ago 2017

@author: davide
'''

'''
    Shows the computation of ecdf:
    Empirical Cumulative Distribution Function
'''

import numpy as np

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / float(n)
    y1 = np.linspace(1.0/float(n), 1.0, num = n)

    print 
    return x, y
