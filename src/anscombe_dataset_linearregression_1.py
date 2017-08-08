'''
Created on 05 ago 2017

@author: davide
'''

'''
    Show linear regression on the first Anscombe data set
'''

import numpy as np
import matplotlib.pyplot as plt

def define_x_y():
    x = np.array(
        [ 10.,   8.,  13.,   9.,  11.,  14.,   6.,   4.,  12.,   7.,   5.]        
        )
    y =np.array(
        [10.,   8.,  13.,   9.,  11.,  14.,   6.,   4.,  12.,   7.,   5.]        
        )
    
    return x, y

x, y = define_x_y()

a, b = np.polyfit(x, y, 1)
print("Slope a: " + str(a) + ", intercept b: " + str(b) + ".")

print("Quality of linear fit: " + str(np.corrcoef(x, y)[0, 1]) + " out of 1.")

_ = plt.plot(x, y, marker='.', linestyle='none')
plt.margins(0.02)

# Make theoretical line to plot
x_interpolated = np.array([np.min(x), np.max(x)])
y_interpolated = a*x_interpolated + b

_ = plt.plot(x_interpolated, y_interpolated)

plt.show()