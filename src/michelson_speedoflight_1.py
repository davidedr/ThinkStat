'''
Created on 04 ago 2017

@author: davide
'''

'''
    Statistical processing of Michelson's Speed of light measurements
    Histogram and distribution comparison with actual normal
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import ecdf

sol = pd.read_csv('michelsons_speedoflight_data.csv')

sns.set()

n_data = sol.shape[0]
print(n_data)
n_bins = int(np.sqrt(n_data))

_ = plt.hist(sol['Velocity'], bins=n_bins)
plt.show()

mean = np.mean(sol['Velocity'])
std = np.std(sol['Velocity'])

'''
    Compare w/ true normal
'''
n_samples= 1E4
samples = np.random.normal(mean, std, size=n_samples)
n_bins_samples = int(np.sqrt(n_samples))

x_sol_ecdf, y_sol_ecdf = ecdf.ecdf(sol['Velocity'])
x_samples_ecdf, y_samples_ecdf = ecdf.ecdf(samples)


_ = plt.plot(x_sol_ecdf, y_sol_ecdf, marker='.', linestyle='none')
_ = plt.plot(x_samples_ecdf, y_samples_ecdf, marker='.', linestyle='none')

# Make nice margins
_ = plt.margins(0.02)

# Annotate the plot
plt.legend(("Michelson's data", 'Normal'), loc='lower right')
_ = plt.xlabel('Velocity')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()
