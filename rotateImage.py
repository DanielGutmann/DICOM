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
    row, column, depth = np.mgrid[-matrix_size:matrix_size + 1, -matrix_size:matrix_size + 1,
                         -int(matrix_size / 2):int(matrix_size / 2) + 1]
    print(rotate_m)
    pixel = []
    for r2, c2, d2 in zip(row, column, depth):
        for i2, j2, z2 in zip(r2, c2, d2):
            for i, j, z in zip(i2, j2, z2):
                pixel.append(np.array([i, j, z]))
                rotated.append(np.dot(np.array([i, j, z]), rotate_m))
    return np.array(rotated), np.array(pixel)


class rotateImage():

    def __init__(self, Image3D):


    def apply(self, spacing, azimuth, elevation, size_of_area):
        azimuth = ((360 - azimuth) * pi) / 180.0
        elevation = ((180-(elevation+90)) * pi) / 180.0
        self.grid, self.pixel = rotation(size_of_area, azimuth, elevation)
        print(azimuth,elevation)
        step_x = spacing[0]
        step_y = spacing[0]
        step_z = spacing[0]

        self.grid[:, 0] = self.grid[:, 0] * step_x
        self.grid[:, 1] = self.grid[:, 1] * step_y
        self.grid[:, 2] = self.grid[:, 2] * step_z

        self.x, self.y, self.z = np.mgrid[np.min(self.grid[:, 0]):np.max(self.grid[:, 0]) + 1:step_x,
                                 np.min(self.grid[:, 1]):np.max(self.grid[:, 1]) + 1:step_y,
                                 np.min(self.grid[:, 2]): np.max(self.grid[:, 2]) + 1:step_z]
        print(np.min(self.x), np.max(self.x))
        print(np.min(self.z), np.max(self.z))


    def apply(self):
        return griddata(self.grid, self.pixel, (self.x, self.y, self.z), method='linear')


if __name__ == "__main__":
    rotateImage([1, 1, 6], 0.0, 0.0, 10).apply().shape