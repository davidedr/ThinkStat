'''
Created on 11 ago 2017

@author: davide
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def sigmoid(x):
    '''
        Computes the sigmoid function for the given value x
    '''
    value = 1/(1 + np.exp(-x))
    return value

print(sigmoid(1E5))
print(1E-5)
print(sigmoid(1E-5))
print(sigmoid(0.00001))

x = np.linspace(-10, 10, int(1E3))
sigma = sigmoid(x)
print(sigma)

sns.set()
_ = plt.plot(x, sigma)
_ = plt.xlabel('x')
_ = plt.ylabel('sigma(x)')
plt.margins(0.02)
plt.show()
