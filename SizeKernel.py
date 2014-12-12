from math import ceil
from matplotlib import cm
from matplotlib.pyplot import figure, show
from scipy.interpolate import interpn, griddata
import numpy as np

__author__ = 'Agnieszka'
from LoGKernel import LoG2D, LoG3D


class SizeKernel2D(object):
    def __init__(self, spacing):
        """
        interpolate kernel values from LoGKernel.LoG2D to smaller mask organ
        :param spacing: spacing is a size of pixel in [mm] taken from spacing = ReadDirWithBinaryData('./test_data/1_nd/').get_spacing()

        """
        self.spacing = spacing

    def __call__(self, mask_size, sigma):
        """

        :param mask_size: size of mask in [mm] should depend on real size od
        :param sigma: sigma is a LoG parameter
        :return: kernel with new size depending on mask_size and spacing and new values
        """
        pixel_size_of_mask = ceil(mask_size / self.spacing[0])
        pixel_size_of_mask = pixel_size_of_mask + ((pixel_size_of_mask - 1) % 2)
        # object for getting log with appropriate sigma
        self.LoG2D = LoG2D(sigma)
        LoG_kernel = self.LoG2D.get_LoG()
        self.x, self.y = self.LoG2D.get_grid_x_y()
        # grid for interpolate value
        index_value = np.linspace(0, self.x.size - 1, pixel_size_of_mask).astype(dtype=np.int)
        index_value[-1] = self.x.size - 1
        max_value_index = np.unravel_index(LoG_kernel.argmax(), LoG_kernel.shape)[0]
        if not (max_value_index in index_value):
            index_value[-2] = max_value_index
            index_value.sort()

        #1D array
        one = np.ones((pixel_size_of_mask,)).astype(dtype=np.int)

        list_for_grid_temp = []
        for i in index_value:
            list_for_grid_temp.append(np.array([self.x[index_value], self.x[i * one]]).T)
        interpolate_grid = np.array(list_for_grid_temp)
        print(interpolate_grid[1], interpolate_grid[1].shape)

        #interpolation
        kernel = interpn((self.x, self.y), LoG_kernel, interpolate_grid)

        return kernel


class SizeKernel3D(object):
    def __init__(self, spacing):
        """
        interpolate kernel values from LoGKernel.LoG2D to smaller mask organ
        :param spacing: spacing is a size of pixel in [mm] taken from spacing = ReadDirWithBinaryData('./test_data/1_nd/').get_spacing()

        """
        self.spacing = spacing

    def __call__(self, mask_size, sigma):
        """

        :param mask_size: size of mask in [mm] should depend on real size od
        :param sigma: sigma is a LoG parameter
        :return: kernel with new size depending on mask_size and spacing and new values
        """
        pixel_size_of_mask = ceil(mask_size / self.spacing[0])
        pixel_size_of_mask = pixel_size_of_mask + ((pixel_size_of_mask - 1) % 2)
        pixel_size_of_mask_z = ceil(mask_size / self.spacing[2])
        pixel_size_of_mask_z = pixel_size_of_mask_z + ((pixel_size_of_mask_z - 1) % 2)
        # object for getting log with appropriate sigma

        self.LoG3D = LoG3D(sigma)
        LoG_kernel = self.LoG3D.get_LoG()
        self.x, self.y, self.z = self.LoG3D.get_grid_x_y_z()
        index_value = np.linspace(0, self.x.size - 1, pixel_size_of_mask).astype(dtype=np.int)
        index_value_z = np.linspace(0, self.x.size - 1, pixel_size_of_mask_z).astype(dtype=np.int)
        index_value[-1] = self.x.size - 1
        max_value_index = np.unravel_index(LoG_kernel.argmax(), LoG_kernel.shape)[0]
        index_value_z[-1] = self.x.size - 1
        max_value_index_z = np.unravel_index(LoG_kernel.argmax(), LoG_kernel.shape)[2]
        if not (max_value_index in index_value):
            index_value[-2] = max_value_index
            index_value.sort()
        if not (max_value_index_z in index_value_z):
            index_value_z[-2] = max_value_index_z
            index_value_z.sort()
        one = np.ones(pixel_size_of_mask_z).astype(dtype=np.int)
        list_end = []

        for j in index_value:
            list_for_grid_temp = []
            for i in index_value:
                list_for_grid_temp.append(np.array([one * self.x[j], one * self.y[i], self.z[index_value_z]]).T)
            list_end.append(list_for_grid_temp)
        interpolate_grid = np.array(list_end)

        kernel = interpn((self.x, self.y, self.z), LoG_kernel, interpolate_grid)
       
        return kernel
