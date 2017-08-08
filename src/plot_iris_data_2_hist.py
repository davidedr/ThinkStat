'''
Created on 03 ago 2017

@author: davide
'''

import sklearn
print('The scikit-learn version is {}.'.format(sklearn.__version__))

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
iris_data = load_iris()

versicolor_petal_length = np.array([ 4.7,  4.5,  4.9,  4. ,  4.6,  4.5,  4.7,  3.3,  4.6,  3.9,  3.5,
        4.2,  4. ,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4. ,
        4.9,  4.7,  4.3,  4.4,  4.8,  5. ,  4.5,  3.5,  3.8,  3.7,  3.9,
        5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4. ,  4.4,  4.6,  4. ,  3.3,
        4.2,  4.2,  4.2,  4.3,  3. ,  4.1]) 
print(type(versicolor_petal_length))
print(versicolor_petal_length)

# Set default Seaborn style
sns.set()

# Compute number of data points: n_data
n_data = len(versicolor_petal_length)
print("versicolor_petal_length has {} elements.", n_data)

# Number of bins is the square root of number of data points: n_bins
n_bins = int(np.sqrt(n_data))
print("bins: " + str(n_bins) + ".")

# Convert number of bins to integer: n_bins
n_bins = int(n_bins)

# Plot histogram of versicolor petal lengths
_ = plt.hist(versicolor_petal_length, bins=n_bins)
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

# Show histogram
plt.show()
