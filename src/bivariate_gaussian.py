'''
Created on 10 ago 2017

@author: davide
'''
from astropy.stats.tests import test_sigma_clipping

'''
    Compute and plot an example of bivariate gaussian distribution
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

N = 60
X = np.linspace(-3, 3, N) 
Y = np.linspace(-3, 4, N)
X, Y = np.meshgrid(X, Y)

# Mean vector and Covariance matrix
mu = np.array([0., 1.])
sigma = np.array([[1., -0.5], [-0.5, 1.5]]) # Should be symmetric and positive definite...

pos = np.empty(X.shape + (2, ))
pos[:, :, 0] = X
pos[:, :, 1] = Y

def multivariate_gaussian(pos, mu, sigma):
    '''
        Return the multivariate gaussian for the position in array pos
    '''
    
    n = mu.shape[0]
    sigma_det = np.linalg.det(sigma)
    sigma_inv = np.linalg.inv(sigma)
    scale_factor = np.sqrt((2*np.pi)**n * sigma_det)
    scale_factor = 1/scale_factor
    fac = np.einsum('...k,kl,...l->...', pos - mu, sigma_inv, pos - mu)
    return np.exp(-fac / 2) * scale_factor
    
Z = multivariate_gaussian(pos, mu, sigma)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, rstride = 3, cstride = 3, linewidth = 1, antialiased=True, cmap = cm.viridis)
cset = ax.contourf(X, Y, Z, zdir = 'z', offset = -0.15, cmap = cm.viridis)

# Adjust the limits, ticks and view angle
ax.set_zlim(-0.15,0.2)
ax.set_zticks(np.linspace(0,0.2,5))
ax.view_init(27, -21)

plt.show()

Z1 = Z

'''
    Now use scipy.stats 
'''
from scipy.stats import multivariate_normal
F = multivariate_normal(mu, sigma)
Z = F.pdf(pos)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, rstride = 3, cstride = 3, linewidth = 1, antialiased=True, cmap = cm.viridis)
cset = ax.contourf(X, Y, Z, zdir = 'z', offset = -0.15, cmap = cm.viridis)

# Adjust the limits, ticks and view angle
ax.set_zlim(-0.15,0.2)
ax.set_zticks(np.linspace(0,0.2,5))
ax.view_init(27, -21)

plt.show()

'''
    Compare the two ways of computing Z
'''
delta = Z1-Z 
print(delta)
print()
print("L2 norm of the difference matrix: " + str(np.linalg.norm(delta)) + " should be (almost) zero...")