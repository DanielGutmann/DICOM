__author__ = 'Agnieszka'

import numpy as np


class KeypointOrientation(object):
    def __init__(self):
        pass

    def keypoints_histograms(self):
        keypoints=0
        Image3D_smoothed=0
        size_of_window = 1
        pixel_x = 0
        pixel_y = 0
        pixel_z = 0
        sigma = 0
        delta_azimuth = 0
        delta_elevation = 0
        pixel_distance = np.arange(-size_of_window, size_of_window + 1)
        X, Y, Z = np.meshgrid(pixel_distance / pixel_x, pixel_distance / pixel_y, pixel_distance / pixel_z)
        gauusian_weight = np.exp(-(X ** 2 + Y ** 2 + Z ** 2) / (2 * sigma ** 2))

        for keypoint in keypoints:
            i = keypoint[0]
            j = keypoint[0]
            z = keypoint[0]
            space3D = Image3D_smoothed[i - size_of_window:i + size_of_window, j - size_of_window:j + size_of_window,
                      z - size_of_window:z + size_of_window]
            # pochodna po mm jak? czy interpolowac wartość dla mniejszego kroku czy liczyc wzglednie
            spacedx = np.diff(space3D, axis=0) / pixel_x
            spacedy = np.diff(space3D, axis=1) / pixel_y
            spacedz = np.diff(space3D, axis=2) / pixel_z
            magnitude = np.sqrt(spacedx ** 2 + spacedy ** 2 + spacedz ** 2)
            azimuth = np.arctan(spacedy / spacedx)
            elevation = np.arctan(spacedz / np.sqrt(spacedy ** 2 + spacedx ** 2)),
            solid_angle = 1 / (delta_elevation * (np.cos(azimuth) - np.cos(azimuth + delta_azimuth)))
            weights = magnitude * gauusian_weight * solid_angle
            np.histogram2d(azimuth, elevation, [4, 8], weights=weights)

