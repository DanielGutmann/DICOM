from scipy.interpolate import griddata, interpn
from Histogram2D import Histogram2D
from Normalization import normalize
from Vizualization import visualization3D_notimage

__author__ = 'Agnieszka'

import numpy as np


def cartesian_coord(*arrays):
    grid = np.meshgrid(*arrays)
    coord_list = [entry.ravel() for entry in grid]
    points = np.vstack(coord_list).T
    return points


class matrixHist(object):
    def __init__(self, mask, spacing):
        self.spacing = spacing
        self.mask = self.interp(mask)
        print(self.mask.shape)
        # do maski
        sigma_x = self.mask.shape[0] * 1.5
        sigma_z = self.mask.shape[2] * 1.5
        x_range = np.arange(0, self.mask.shape[0] / 2 + 1)
        self.pixel_distance_x = np.sort(np.concatenate((-x_range[1:], x_range)))
        z_range = np.arange(0, self.mask.shape[2] / 2 + 1)
        self.pixel_distance_z = np.sort(np.concatenate((-z_range[1:], z_range)))
        # maska poprawna codo wartosci
        self.X, self.Y, self.Z = np.meshgrid(self.pixel_distance_x, self.pixel_distance_x,
                                             self.pixel_distance_z)

        self.gaussian_weight = np.exp(
            -((self.X ** 2 + self.Y ** 2) / (2 * (sigma_x ** 2)) + (self.Z ** 2) / (2 * (sigma_z ** 2))))
        print(self.gaussian_weight.shape)


    def interp(self, mask):
        # w mm
        new_grid_range_x = np.arange(0, 8, 1)
        new_grid_range_z = np.arange(0, 8, 1)
        new_pixel_distance_x = np.sort(np.concatenate((-new_grid_range_x[1:], new_grid_range_x)))
        new_pixel_distance_z = np.sort(np.concatenate((-new_grid_range_z[1:], new_grid_range_z)))

        grid_range_x = np.arange(0, (mask.shape[0] / 2.) * self.spacing[0], self.spacing[0])
        grid_range_z = np.arange(0, (mask.shape[2] / 2.) * self.spacing[2], self.spacing[2])
        pixel_distance_x = np.sort(np.concatenate((-grid_range_x[1:], grid_range_x)))
        pixel_distance_z = np.sort(np.concatenate((-grid_range_z[1:], grid_range_z)))

        x, y, z = np.meshgrid(new_pixel_distance_x, new_pixel_distance_x, new_pixel_distance_z, indexing='ij')

        interpolate_grid = np.array([x[:, :, :], y[:, :, :], z[:, :, :]]).T

        new_mask = interpn((pixel_distance_x, pixel_distance_x, pixel_distance_z ), mask, interpolate_grid)
        return new_mask.T

    def apply(self):
        delta_azimuth = np.pi / 4.
        delta_elevation = np.pi / 4.
        dx, dy, dz = np.gradient(self.mask)
        self.magnitude = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        self.azimuth = np.arctan2(dy, dx) + np.pi
        self.elevation = np.arctan2(dz, np.sqrt(dx ** 2 + dy ** 2)) + np.pi / 2
        solid_angle = 1 / (delta_elevation * (np.cos(self.azimuth) - np.cos(self.azimuth + delta_azimuth)))
        solid_angle = normalize(solid_angle, [np.min(solid_angle), np.max(solid_angle)], [0, 1])
        self.magnitude = normalize(self.magnitude, [np.min(self.magnitude), np.max(self.magnitude)], [0, 1])
        self.gaussian_weight = normalize(self.gaussian_weight, [np.min(self.gaussian_weight),
                                                                np.max(self.gaussian_weight)], [0, 1])
        weights = self.magnitude * self.gaussian_weight * solid_angle
        self.weights = normalize(weights, [np.min(weights), np.max(weights)], [0, 1])
        NO_xbin = 4
        NO_ybin = 8
        # tu w forze jako 4 czesci macierzy
        self.mask = np.zeros((15, 15, 15))
        self.mask[0, 0, 0] = 255
        self.mask[14, 14, 14] = 255
        self.mask[0, 14, 0] = 255
        self.mask[14, 0, 0] = 255
        self.mask[0, 0, 14] = 255
        self.mask[14, 0, 14] = 255
        self.mask[0, 14, 14] = 255
        self.mask[14, 14, 0] = 255

        div0 = np.array([8, ])
        div1 = np.array([7, ])
        h0 = np.hsplit(self.mask, div0)[0]
        H_1 = np.dsplit(np.vsplit(h0, div0)[0], div0)[0]  # 1
        H_2 = np.dsplit(np.vsplit(h0, div0)[0], div1)[1]  # 2
        H_3 = np.dsplit(np.vsplit(h0, div1)[1], div0)[0]  # 3
        H_4 = np.dsplit(np.vsplit(h0, div1)[1], div1)[1]  #
        h1 = np.hsplit(self.mask, div1)[1]
        H_5 = np.dsplit(np.vsplit(h1, div0)[0], div0)[0]  # 5
        H_6 = np.dsplit(np.vsplit(h1, div0)[0], div1)[1]  # 6
        H_7 = np.dsplit(np.vsplit(h1, div1)[1], div0)[0]  # 7
        H_8 = np.dsplit(np.vsplit(h1, div1)[1], div1)[1]  # 8
        for i in range(1,9):
            visualization3D_notimage(eval('H_'+str(i)))
        H2D = Histogram2D(NO_xbin, NO_ybin)
        H2D.apply(self.elevation, self.azimuth, weights)
        # self.H2D = H2D.get_Histogram2D()
        # zwrocic deskryprot dla keypointu dzies zbierac do listy i zapisac jako obraz




