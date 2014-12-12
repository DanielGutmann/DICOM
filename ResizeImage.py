from scipy.interpolate import interpn
import numpy as np
from scipy.misc import imresize

__author__ = 'Agnieszka'


class ResizeImage2D(object):
    def __init__(self, resize_factor=2):
        self.resize_factor = resize_factor

    def apply(self, image2D):
        x = np.arange(0, image2D.shape[0]).astype(np.float)

        index_value = np.linspace(0, x.size - 1, int(x.size / 2)).astype(dtype=np.int)
        index_value[-1] = x.size - 1
        # 1D array


        one = np.ones((int(x.size / 2),)).astype(dtype=np.int)
        list_for_grid_temp = []
        for i in index_value:
            list_for_grid_temp.append(np.array([x[index_value], x[i * one]]).T)
        interpolate_grid = np.array(list_for_grid_temp)
        # g0wno testy
        image_after_resized = interpn((x, x), image2D, interpolate_grid, bounds_error=True,
                                        fill_value=np.float32(0.0))
        return image_after_resized


class ResizeImage3D(object):
    def __init__(self, resize_factor=2):
        self.resize_factor = resize_factor

    def apply(self, image3D):
        x = np.arange(0, image3D.shape[0]).astype(np.float)
        z = np.arange(0, image3D.shape[2]).astype(np.float)
        index_value = np.linspace(0, x.size - 1, int(x.size / 2)).astype(dtype=np.int)
        index_value[-1] = x.size - 1
        # 1D array

        index_value_z = np.linspace(0, z.size - 1, int(z.size / 2)).astype(dtype=np.int)
        index_value_z[-1] = z.size - 1
        one = np.ones(int(z.size / 2)).astype(dtype=np.int)
        list_end = []

        for j in index_value:
            list_for_grid_temp = []
            for i in index_value:
                list_for_grid_temp.append(np.array([one * x[j], one * x[i], z[index_value_z]]).T)
            list_end.append(list_for_grid_temp)
        interpolate_grid = np.array(list_end)
        # g0wno testy
        image_after_resized = interpn((x, x, z), image3D, interpolate_grid, bounds_error=True,
                                        fill_value=np.float32(0.0))
        return image_after_resized
