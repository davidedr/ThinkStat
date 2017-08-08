'''
Created on 05 ago 2017

@author: davide
'''

'''
    Perform some EDA on the two numeric columns of the dataset
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def histogram(df, colname, title = 'Histogram', xlabel = 'xlabel', ylabel = 'frequency', n_bins = None):
    '''
        Plot histogram for colname column in df dataframe 
    '''
    n = df[colname].count()
    print('col: ' + colname + ' has: ' + str(n) + ' non-null objects out of: ' + str(df.shape[0]) + ' values.')
    
    col_dropna = df[colname].dropna()
    if n_bins == None:
        plt.hist(col_dropna)
    else:
        plt.hist(col_dropna, bins = n_bins)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

df = pd.read_csv("./../Machine Learning with the Experts/TrainingData.csv", index_col = 0)

print("info: ----------------------")
print(df.info())
print()

print("head: ----------------------")
print(df.head())
print()

print("describe: ----------------------")
print(df.describe())
print()

sns.set()

colname = 'FTE'
histogram(df, colname, title = 'Distribution of %full-time \n employee works', xlabel = '% of full-time', ylabel = 'num employees')

colname = 'Total'
histogram(df, colname, title = 'Distribution of Total cost of expenditure \n How much does the budget item cost?', xlabel = '', ylabel = 'USD', n_bins = 39)

'''
    Encode labels (objects) as categories
'''
print(df.use)