from math import ceil, pi
from mayavi import mlab
from Normalization import keypoints_concatenate, normalize
from ReadImage import ReadImage

__author__ = 'Agnieszka'

import numpy as np


class KeyPointOrientation(object):
    def __init__(self, path):
        path_for_keypoints = path + '/Hessian3D/'
        path_for_Gaussian = path + '/3DGaussianSmoothing'
        self.ImageReader = ReadImage(path_for_Gaussian)
        self.PointReader = ReadImage(path_for_keypoints)
        self.list_with_keyponits = self.PointReader.openImage()
        self.spacing = self.list_with_keyponits[0].spacing
        sigma_x = 4  # list_with_keyponits[0].sigma * 2 mask size is 9
        self.size_in_pixels_xy = ceil(sigma_x)

        x_range = np.arange(0, self.size_in_pixels_xy + 1)
        self.pixel_distance_x = np.sort(np.concatenate((-x_range[1:], x_range)))
        self.size_of_window_x = self.size_in_pixels_xy
        self.size_of_window_z = self.size_in_pixels_xy
        self.X, self.Y, self.Z = np.meshgrid(self.pixel_distance_x, self.pixel_distance_x,
                                             self.pixel_distance_x)
        # self.X, self.Y = np.meshgrid(self.pixel_distance_x, self.pixel_distance_x)
        # to dla 1.5 sigmy

        self.gaussian_weight = np.exp(-((self.X ** 2 + self.Y ** 2 + self.Z ** 2) / (2 * (sigma_x / 2) ** 2)))

    def apply(self):
        list_with_GaussianImages = self.ImageReader.openImage()
        for i in range(0, len(self.list_with_keyponits)):
            self.keypoints_histograms(list_with_GaussianImages[i + 1], self.list_with_keyponits[i])


    def keypoints_histograms(self, image3D_agregator, keypooints_agregator):
        # diff in [mm space]
        dx, dy, dz = np.gradient(image3D_agregator.Image3D, image3D_agregator.spacing[0], image3D_agregator.spacing[1],
                                 image3D_agregator.spacing[2])

        keypoints = keypoints_concatenate(keypooints_agregator)

        # do konfigracji
        delta_azimuth = np.pi / 2.
        delta_elevation = np.pi / 2
        i = 0
        for k in range(0, keypoints.shape[0]):

            i = keypoints[k][0]
            j = keypoints[k][1]
            z = keypoints[k][2]

            temp_x = dx[i - self.size_of_window_x:i + self.size_of_window_x + 1,
                     j - self.size_of_window_x:j + self.size_of_window_x + 1,
                     z - self.size_of_window_z:z + self.size_of_window_z + 1]

            if temp_x.shape[0] != 2 * self.size_in_pixels_xy + 1:  continue
            if temp_x.shape[1] != 2 * self.size_in_pixels_xy + 1:  continue
            if temp_x.shape[2] != 2 * self.size_in_pixels_xy + 1:  continue

            temp_z = dz[i - self.size_of_window_x:i + self.size_of_window_x + 1,
                     j - self.size_of_window_x:j + self.size_of_window_x + 1,
                     z - self.size_of_window_z:z + self.size_of_window_z + 1]
            if temp_z.shape[0] != 2 * self.size_in_pixels_xy + 1:  continue
            if temp_z.shape[1] != 2 * self.size_in_pixels_xy + 1:  continue
            if temp_z.shape[2] != 2 * self.size_in_pixels_xy + 1:  continue

            self.magnitude = np.sqrt(dx[i - self.size_of_window_x:i + self.size_of_window_x + 1,
                                     j - self.size_of_window_x:j + self.size_of_window_x + 1,
                                     z - self.size_of_window_z:z + self.size_of_window_z + 1] ** 2 + dy[
                                                                                                     i - self.size_of_window_x:i + self.size_of_window_x + 1,
                                                                                                     j - self.size_of_window_x:j + self.size_of_window_x + 1,
                                                                                                     z - self.size_of_window_z:z + self.size_of_window_z + 1] ** 2 + dz[

                                                                                                                                                                     i - self.size_of_window_x:i + self.size_of_window_x + 1,
                                                                                                                                                                     j - self.size_of_window_x:j + self.size_of_window_x + 1,
                                                                                                                                                                     z - self.size_of_window_z:z + self.size_of_window_z + 1] ** 2)

            self.azimuth = np.arctan2(dy[i - self.size_of_window_x:i + self.size_of_window_x + 1,
                                      j - self.size_of_window_x:j + self.size_of_window_x + 1,
                                      z - self.size_of_window_z:z + self.size_of_window_z + 1], dx[
                                                                                                i - self.size_of_window_x:i + self.size_of_window_x + 1,
                                                                                                j - self.size_of_window_x:j + self.size_of_window_x + 1,
                                                                                                z - self.size_of_window_z:z + self.size_of_window_z + 1]) + np.pi

            self.elevation = np.arccos(dz[i - self.size_of_window_x:i + self.size_of_window_x + 1,
                                       j - self.size_of_window_x:j + self.size_of_window_x + 1,
                                       z - self.size_of_window_z:z + self.size_of_window_z + 1] / self.magnitude)

            solid_angle = 1 / (delta_elevation * (np.cos(self.azimuth) - np.cos(self.azimuth + delta_azimuth)))

            weights = self.magnitude * self.gaussian_weight * solid_angle
            self.weights = normalize(weights, [np.max(weights), np.min(weights)], [0, 1])


        return self.azimuth, self.elevation, self.weights




