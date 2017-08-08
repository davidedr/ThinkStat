'''
Created on 03 ago 2017

@author: davide
'''

'''
    Shows the use of bee swarm plot
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

iris_data_df = pd.DataFrame.from_csv('iris_data_df.csv')
print(iris_data_df.head)

x_data = iris_data_df['species']
y_data = iris_data_df['petal length (cm)']

_ = sns.swarmplot(x_data, y_data)
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')
plt.show()


'''
    Shorter way:
    sns.swarmplot(x='species', y='petal length (cm)', data=iris_data_df)
'''