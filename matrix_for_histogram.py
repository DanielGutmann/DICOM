from Histogram2D import Histogram2D
from Normalization import normalize

__author__ = 'Agnieszka'

import numpy as np

class matrixHist(object):

    def __init__(self,mask,spacing):
        self.mask=mask
        self.spacng=spacing
        sigma_x=2
        gasussian do porawienia w zalznosci od roziaru maski
        x_range = np.arange(0, self.mask.shape[0] + 1)
        self.pixel_distance_x = np.sort(np.concatenate((-x_range[1:], x_range)))
        self.size_of_window_x = self.size_in_pixels_xy
        self.size_of_window_z = self.size_in_pixels_xy
        self.X, self.Y, self.Z = np.meshgrid(self.pixel_distance_x, self.pixel_distance_x,
                                             self.pixel_distance_x)
        # self.X, self.Y = np.meshgrid(self.pixel_distance_x, self.pixel_distance_x)
        # to dla 1.5 sigmy

        self.gaussian_weight = np.exp(-((self.X ** 2 + self.Y ** 2 + self.Z ** 2) / (2 * (sigma_x / 2) ** 2)))
        pass
    def apply(self):
        delta_azimuth = np.pi / 4.
        delta_elevation = np.pi / 4.
        dx,dy,dz =np.gradient(self.mask,self.spacng[0],self.spacng[1],self.spacng[2])
        self.magnitude = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        self.azimuth = np.arctan2(dy, dx) + np.pi
        self.elevation = np.arctan2(dz,np.sqrt(dx ** 2 + dy ** 2))+np.pi/2
        solid_angle = 1 / (delta_elevation * (np.cos(self.azimuth) - np.cos(self.azimuth + delta_azimuth)))
        solid_angle = normalize(solid_angle, [np.min(solid_angle), np.max(solid_angle)], [0, 1])
        self.magnitude = normalize(self.magnitude, [np.min(self.magnitude), np.max(self.magnitude)], [0, 1])

        self.gaussian_weight = normalize(self.gaussian_weight, [np.min(self.gaussian_weight),
                                                                    np.max(self.gaussian_weight)], [0, 1])
        weights = self.magnitude * self.gaussian_weight * solid_angle
        self.weights = normalize(weights, [np.min(weights), np.max(weights)], [0, 1])
        NO_xbin = 4
        NO_ybin = 8

        H2D = Histogram2D(NO_xbin, NO_ybin)
        H2D.apply(self.elevation, self.azimuth, weights)
        self.H2D = H2D.get_Histogram2D()




