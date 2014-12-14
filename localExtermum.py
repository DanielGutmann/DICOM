__author__ = 'Agnieszka'

import numpy as np


class LocalExterma3D(object):
    def __init__(self):
        """
        Find local extrema without edges in one image
        """
        self.true_array = np.ones((3, 3, 3), dtype=np.bool)
        self.true_array[1, 1, 1] = False
        self.false_array = -self.true_array
        self.min_list = []
        self.max_list = []

    def find(self, image3D):
        """

        :param image3D: image after convolution LoG
        :return: void
        """

        shape = image3D.shape()

        for i in range(1, shape[0]):
            for j in range(1, shape[1]):
                for z in range(1, shape[2]):
                    value_for_extrema = image3D[i, j, z]
                    bool_array = value_for_extrema < image3D[i - 1:i + 2, j - 1:j + 2, z - 1:z + 2]

                    if np.array_equal(bool_array, self.true_array):
                        self.min_list.append(np.array[i, j, z])
                    elif np.array_equal(bool_array, self.false_array):
                        self.max_list.append(np.array[i, j, z])

    def get_min_max(self):
        """
        :return: list of indexes as a np.array min and max [i,j,z]
        """
        return np.array(self.min_list), np.array(self.max_list)



