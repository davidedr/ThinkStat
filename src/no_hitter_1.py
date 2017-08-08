'''
Created on 04 ago 2017

@author: davide
'''

'''
    Show comparison of ecdfs between a supposedly Poisson time series
    and a computed Poisson time series
    The value of the parameter tau that makes the exponential distribution best match the data
    is the mean interval time (where time is in units of number of games) between no-hitters.
    The (normalized) histogram is plotted as an approximation of the PDF
    The ECDF plots show that there's almost a perfect fit.
    As a amtter of fact, two other exponential distributions are generated, one having half tau
    as the parameter and another having double tau.
    Plotting the ECDFs and comparing it with the sample data's ECDF we check that
    those are not quite fitting the sampled data. And so the tau we get as the average of the samples
    is the parameter for the exp distribution in order to fit the data.  
'''

import numpy as np
import matplotlib.pyplot as plt

import ecdf as ecdf

def define_no_hitter_times():
    '''
    Number of games played between ech no-hitter in the modern era (1901-2015)
    of Major League Baseball  
    '''
    nohitter_times = np.array(
        [843, 1613, 1101,  215,  684,  814,  278,  324,  161,  219,  545,
        715,  966,  624,   29,  450,  107,   20,   91, 1325,  124, 1468,
        104, 1309,  429,   62, 1878, 1104,  123,  251,   93,  188,  983,
        166,   96,  702,   23,  524,   26,  299,   59,   39,   12,    2,
        308, 1114,  813,  887,  645, 2088,   42, 2090,   11,  886, 1665,
       1084, 2900, 2432,  750, 4021, 1070, 1765, 1322,   26,  548, 1525,
         77, 2181, 2752,  127, 2147,  211,   41, 1575,  151,  479,  697,
        557, 2267,  542,  392,   73,  603,  233,  255,  528,  397, 1529,
       1023, 1194,  462,  583,   37,  943,  996,  480, 1497,  717,  224,
        219, 1531,  498,   44,  288,  267,  600,   52,  269, 1086,  386,
        176, 2199,  216,   54,  675, 1243,  463,  650,  171,  327,  110,
        774,  509,    8,  197,  136,   12, 1124,   64,  380,  811,  232,
        192,  731,  715,  226,  605,  539, 1491,  323,  240,  179,  702,
        156,   82, 1397,  354,  778,  603, 1001,  385,  986,  203,  149,
        576,  445,  180, 1403,  252,  675, 1351, 2983, 1568,   45,  899,
       3260, 1025,   31,  100, 2055, 4043,   79,  238, 3931, 2351,  595,
        110,  215,    0,  563,  206,  660,  242,  577,  179,  157,  192,
        192, 1848,  792, 1693,   55,  388,  225, 1134, 1172, 1555,   31,
       1582, 1044,  378, 1687, 2915,  280,  765, 2819,  511, 1521,  745,
       2491,  580, 2072, 6450,  578,  745, 1075, 1103, 1549, 1520,  138,
       1202,  296,  277,  351,  391,  950,  459,   62, 1056, 1128,  139,
        420,   87,   71,  814,  603, 1349,  162, 1027,  783,  326,  101,
        876,  381,  905,  156,  419,  239,  119,  129,  467])
    return nohitter_times   

nohitter_times = define_no_hitter_times()

# Seed random number generator
np.random.seed(42)

# Compute mean no-hitter time: tau
tau = np.mean(nohitter_times)

# Draw out of an exponential distribution with parameter tau: inter_nohitter_time
inter_nohitter_time = np.random.exponential(tau, 100000)

# Plot the PDF and label axes
_ = plt.hist(nohitter_times,bins=50, normed=True, histtype='step')
_ = plt.hist(inter_nohitter_time,bins=50, normed=True, histtype='step')
plt.legend(("No hitter times", 'Exponential'), loc='lower right')
_ = plt.xlabel('Games between no-hitters')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()

x_nohitter_times, y_nohitter_times = ecdf.ecdf(nohitter_times)
x_inter_nohitter_time, y_inter_nohitter_time = ecdf.ecdf(inter_nohitter_time)
_ = plt.plot(x_nohitter_times, y_nohitter_times, marker='.', linestyle='none')
_ = plt.plot(x_inter_nohitter_time, y_inter_nohitter_time, marker='.', linestyle='none')
plt.legend(("No hitter times", 'Exponential'), loc='lower right')
_ = plt.xlabel('Games between no-hitters')
_ = plt.ylabel('ECDF')

# Make nice margins
_ = plt.margins(0.02)

plt.show()

'''
    Now "verify" that the selected tau (i. e., the mean of the samples) is the "best"
    parameter to use to draw samples form ax exponential distribution 
'''
# Take samples with half tau: samples_half
samples_half = np.random.exponential(tau/2, 100000)

# Take samples with double tau: samples_double
samples_double = np.random.exponential(tau*2, 100000)

# Take samples with double tau: samples_double
x_half, y_half = ecdf.ecdf(samples_half)
x_double, y_double = ecdf.ecdf(samples_double)
_ = plt.plot(x_nohitter_times, y_nohitter_times, marker='.', linestyle='none')
_ = plt.plot(x_half, y_half, marker='.', linestyle='none')
_ = plt.plot(x_double, y_double, marker='.', linestyle='none')
plt.legend(("No hitter times - Sample data", 'Half tau', 'Double tau'), loc='lower right')
_ = plt.xlabel('Games between no-hitters')
_ = plt.ylabel('ECDF')
# Make nice margins
_ = plt.margins(0.02)

plt.show()
