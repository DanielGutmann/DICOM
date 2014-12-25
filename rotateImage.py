__author__ = 'Agnieszka'
from math import pi
from scipy.interpolate import interpn, Rbf, griddata
import numpy as np


def rotate_matrix(azimuth, elevation):
    return np.array([[np.cos(azimuth) * np.cos(elevation), -np.sin(azimuth), -np.cos(azimuth) * np.sin(elevation)],
                     [np.sin(azimuth) * np.cos(elevation), np.cos(azimuth), -np.sin(azimuth) * np.sin(elevation)],
                     [np.sin(elevation), 0, np.cos(elevation)]])


def rotation(matrix_size, azimuth, elevation):
    rotate_m = rotate_matrix(azimuth, elevation)
    rotated = []
    pixel = []
    for i in range(-matrix_size, matrix_size + 1, 1):
        for j in range(-matrix_size, matrix_size + 1, 1):
            for z in range(-int(matrix_size / 3), int(matrix_size / 3) + 1, 1):
                pixel.append(np.array([i, j, z]))
                rotated.append(np.dot(np.array([i, j, z]), rotate_m))
    return np.array(rotated), np.array(pixel)


class rotateImage():
    def __init__(self, Image3D):
        self.image3D = Image3D


    def apply(self, azimuth, elevation, size_of_area):
        self.grid, self.pixel_index = rotation(size_of_area, azimuth, elevation)

        step_x = self.image3D.spacing[0]
        step_y = self.image3D.spacing[1]
        step_z = self.image3D.spacing[2]
        self.pixel_index[:, 0] = self.pixel_index[:, 0] + 256
        self.pixel_index[:, 1] = self.pixel_index[:, 1] + 256
        self.pixel_index[:, 2] = self.pixel_index[:, 2] + 37
        self.grid[:, 0] = self.grid[:, 0] + 256
        self.grid[:, 1] = self.grid[:, 1] + 256
        self.grid[:, 2] = self.grid[:, 2] + 37
        #self.grid[:, 0] = self.grid[:, 0] * step_x
        #self.grid[:, 1] = self.grid[:, 1] * step_y
        #self.grid[:, 2] = self.grid[:, 2] * step_z


        self.x, self.y, self.z = np.mgrid[-8:8, -8:8, -2:2]
        self.x = self.x + 256
        self.y = self.y + 256
        self.z = self.z + 37

        im = self.imageInterp()
        return im

    def imageInterp(self):
        return griddata(self.grid, self.image3D.get_image3D()[
            self.pixel_index[:, 0], self.pixel_index[:, 1], self.pixel_index[:, 2]]
                        ,(self.x, self.y, self.z), method='linear')
