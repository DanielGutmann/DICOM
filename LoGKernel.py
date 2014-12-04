from math import pi
from scipy import ndimage
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt

import numpy as np
# LoG=LoGcontatnt*(r^2/sigma^2 -3)*e^-r^2/(2*sigma^2) ,where r is in [mm]

fig = plt.figure()
ax = fig.gca(projection='3d')

x, y, z = np.zeros((3, 3, 3))
sigma = 2
class LoG(object):
    def __init__(self):

        x = np.arange(-100, 100, 0.5)
        y = np.arange(-100, 100, 0.5)
        z = np.arange(-100, 100, 0.5)
        self.X, self.Y, self.Z = np.meshgrid(x, y ,z)


    def __call__(self, sigma):

        sigma_square = sigma ** 2
        LoGcontant = 1.0 / (2.0 * pi * sigma_square ** 2)
        R_square = x ** 2 + y ** 2 + z ** 2
        LoG = LoGcontant * (R_square / sigma_square - 3) * np.exp(-R_square / 2 * sigma_square)
        LoG_normalized = LoG / np.sum(LoG)
        return LoG_normalized



surf = ax.plot_surface(X, Y, k, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

plt.show()