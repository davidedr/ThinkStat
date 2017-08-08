'''
Created on 04 ago 2017

@author: davide
'''

import matplotlib.pyplot as plt
import ecdf

'''
    Show the creation of ECDF plots
'''

versicolor_petal_length = [ 4.7,  4.5,  4.9,  4. ,  4.6,  4.5,  4.7,  3.3,  4.6,  3.9,  3.5,
        4.2,  4. ,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4. ,
        4.9,  4.7,  4.3,  4.4,  4.8,  5. ,  4.5,  3.5,  3.8,  3.7,  3.9,
        5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4. ,  4.4,  4.6,  4. ,  3.3,
        4.2,  4.2,  4.2,  4.3,  3. ,  4.1]

# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf.ecdf(versicolor_petal_length)
print(x_vers)
print(y_vers)

# Generate plot
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')

# Make the margins nice
_ = plt.margins(0.02)

# Label the axes
_ = plt.ylabel('ECDF')
_ = plt.xlabel('Iris Versicolor Petal Length [cm]')

# Display the plot
plt.show()
