from math import ceil, pi
from ReadImage import ReadImage

__author__ = 'Agnieszka'

import numpy as np


class KeyPointOrientation(object):
    def __init__(self, path):
        path_for_keypoints=path+'/Hessian3D/'
        path_for_Gaussian=path+'/3DGaussianSmoothing'
        self.ImageReader = ReadImage(path_for_Gaussian)
        self.PointReader = ReadImage(path_for_keypoints)

    def apply(self):

        list_with_keyponits = self.PointReader.openImage()
        list_with_GaussianImages = self.ImageReader.openImage()
        for i in range(0, len(list_with_keyponits)):
            self.spacing = list_with_keyponits[i].spacing
            sigma_x = list_with_keyponits[i].sigma * 1.5
            sigma_z = ((list_with_keyponits[i].sigma )/(self.spacing[2]/self.spacing[0])) *1.5

            size_in_pixels_xy = sigma_x
            size_in_pixels_z = sigma_z
            print(size_in_pixels_z)
            self.size_of_window_x = size_in_pixels_xy  # ceil(size_in_mm / spacing[0])
            self.size_of_window_y = size_in_pixels_xy  # ceil(size_in_mm / spacing[1])
            self.size_of_window_z = size_in_pixels_z  # ceil(size_in_mm / spacing[2])

            self.pixel_distance_x = np.arange(-self.size_of_window_x*3, self.size_of_window_x*3 + 1)
            self.pixel_distance_z = np.arange(-self.size_of_window_z*3, self.size_of_window_z*3 + 1)

            self.X, self.Y, self.Z = np.meshgrid(self.pixel_distance_x*size_in_pixels_x , self.pixel_distance_x*size_in_pixels_x ,
            self.pixel_distance_z*size_in_pixels_z  )


            self.gaussian_weight = np.exp(-(self.X ** 2 + self.Y ** 2) / (2 * sigma_x ** 2) + ((self.Z ** 2) / (2 * sigma_z ** 2)))



    def keypoints_histograms(self ):
        image3d_smoothed=0
        keypoints=0
        delta_azimuth = np.pi / 2.
        delta_elevation = np.pi / 2
        # diff in [mm space]
        spacedx = (np.diff(image3d_smoothed, axis=0) / self.spacing[0])[:, :-1, :-1]
        spacedy = (np.diff(image3d_smoothed, axis=1) / self.spacing[1])[:-1, :, :-1]
        spacedz = (np.diff(image3d_smoothed, axis=2) / self.spacing[2])[:-1, :-1, :]

        for keypoint in keypoints:
            i = keypoint[0]
            j = keypoint[1]
            z = keypoint[2]
            shape = spacedx.shape
            if (i > shape[0] - self.size_of_window_x - 1 or i < self.size_of_window_x):
                break
            if (j > shape[1] - self.size_of_window_x - 1 or j < self.size_of_window_x):
                break
            if (z > shape[2] - self.size_of_window_x - 1 or z < self.size_of_window_x):
                break

            self.magnitude = np.sqrt(spacedx[i - self.size_of_window_x:i + self.size_of_window_x + 1,
                                     j - self.size_of_window_x:j + self.size_of_window_x + 1,
                                     z - self.size_of_window_z:z + self.size_of_window_z + 1] ** 2 + spacedy[
                                                                                                     i - self.size_of_window_x:i + self.size_of_window_x + 1,
                                                                                                     j - self.size_of_window_x:j + self.size_of_window_x + 1,
                                                                                                     z - self.size_of_window_z:z + self.size_of_window_z + 1] ** 2 + spacedz[

                                                                                                                                                                     i - self.size_of_window_x:i + self.size_of_window_x + 1,
                                                                                                                                                                     j - self.size_of_window_x:j + self.size_of_window_x + 1,
                                                                                                                                                                     z - self.size_of_window_z:z + self.size_of_window_z + 1] ** 2)

            self.azimuth = np.arctan2(spacedy[i - self.size_of_window_x:i + self.size_of_window_x + 1,
                                      j - self.size_of_window_x:j + self.size_of_window_x + 1,
                                      z - self.size_of_window_z:z + self.size_of_window_z + 1], spacedx[
                                                                                                i - self.size_of_window_x:i + self.size_of_window_x + 1,
                                                                                                j - self.size_of_window_x:j + self.size_of_window_x + 1,
                                                                                                z - self.size_of_window_z:z + self.size_of_window_z + 1]) + np.pi

            self.elevation = np.arccos(spacedz[i - self.size_of_window_x:i + self.size_of_window_x + 1,
                                       j - self.size_of_window_x:j + self.size_of_window_x + 1,
                                       z - self.size_of_window_z:z + self.size_of_window_z + 1] / self.magnitude)

            solid_angle = 1 / (delta_elevation * (np.cos(self.azimuth) - np.cos(self.azimuth + delta_azimuth)))

            self.weights = self.magnitude * self.gaussian_weight * solid_angle

            return self.azimuth, self.elevation, self.weights



