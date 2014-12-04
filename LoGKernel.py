from math import pi
from scipy import ndimage
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt

import numpy as np
# LoG=LoGcontatnt*(r^2/sigma^2 -3)*e^-r^2/(2*sigma^2) ,where r is in [mm]

class LoG(object):
    def __init__(self,sigma):
        three_sigma= 3.0*sigma
        self.sigma=sigma
        x = np.arange(-three_sigma,three_sigma, 0.1)
        y = np.arange(-three_sigma,three_sigma, 0.1)
        z = np.arange(-three_sigma,three_sigma, 0.1)

        self.X, self.Y, self.Z= np.meshgrid(x, y,z )



    def __call__(self, sigma):

        sigma_square = self.sigma ** 2
        LoGcontant = 1.0 / (2.0 * pi * (sigma_square ** 2))
        R_square = self.X ** 2 + self.Y ** 2+self.Z ** 2

        exponetnta=np.exp(-R_square /(2 * sigma_square))
        LoG = LoGcontant * (R_square / sigma_square - 2) * exponetnta
        LoG_normalized = LoG/np.sum(LoG)

        return LoG_normalized


class LoG2D(object):
    def __init__(self,sigma):
        three_sigma= 3.0*sigma
        self.sigma=sigma
        x = np.arange(-three_sigma,three_sigma, 0.1)
        y = np.arange(-three_sigma,three_sigma, 0.1)


        self.X, self.Y= np.meshgrid(x, y )


    def __call__(self):

        sigma_square = self.sigma ** 2
        LoGcontant = 1.0 / (2.0 * pi * (sigma_square ** 2))
        R_square = self.X ** 2 + self.Y ** 2

        exponetnta=np.exp(-R_square /(2 * sigma_square))
        LoG = LoGcontant * (R_square / sigma_square - 2) * exponetnta
        LoG_normalized = LoG/np.sum(LoG)
        print np.sum(LoG_normalized)
        return LoG_normalized
