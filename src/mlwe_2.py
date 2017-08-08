'''
Created on 06 ago 2017

@author: davide
'''

'''
    Perform some EDA on the object columns of the dataset
    Show hot to convert generic string columns to categories
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

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

print("dtypes: ----------------------")
print(df.dtypes)
print()

print("dtypes.value_counts: ----------------------")
print(df.dtypes.value_counts())
print()

print(df.Function.unique())
print
print(df.Function.describe())
print()
print(df.Function.astype('category'))
print()

'''
    Modify the column in place. A process known as "creating dummy variables'
'''
print('Convert Function column from object to category, i. e. create dummy variables...')
df.Function = df.Function.astype('category')
print(df.Function.describe())
print()
dummies = pd.get_dummies(df.Function, prefix_sep = '_')
print(dummies)

''' Have a look at each col's datatype '''
print(df.dtypes)
print(df.dtypes.value_counts())

'''
    Apply to every object column in the dataset
'''

''' Convert single column to categorical '''
print()
print('Convert Use and Sharing column from object to category using the lambda...') 
categorize_label = lambda x: x.astype('category')

cols = ['Use', 'Sharing']
df[cols] = df[cols].apply(categorize_label, axis = 0)
print(df.dtypes)
print(df.dtypes.value_counts())

'''
    Compute and plot the number of unique labels for each object column
'''
LABELS = ['Function', 'Use', 'Sharing', 'Reporting', 'Student_Type', 'Position_Type', 'Object_Type', 'Pre_K', 'Operating_Status']
df[LABELS] = df[LABELS].apply(categorize_label, axis = 0)
num_unique_labels = df[LABELS].apply(pd.Series.nunique, axis = 0)
num_unique_labels.plot(kind = 'bar')

# Label the axes
plt.xlabel('Labels')
plt.ylabel('Number of unique values')

# Display the plot
plt.show()