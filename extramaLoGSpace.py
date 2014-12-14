from localExtermum import LocalExterma3D

__author__ = 'Agnieszka'
import numpy as np


class ExtremaLoGSpace3D(object):
    def __init__(self):
        """
        Find local extrema without edges in LoG space
        """
        self.true_array = np.ones((3, 3, 3), dtype=np.bool)
        self.min_list = []
        self.max_list = []
        self.local_extrema = LocalExterma3D()


    def find(self, list_with_three_images_3D):
        """

        :param list_with_three_images_3D: list with three images as np.array after LoG in LoG space direction with increasing sigma
        :return: void
        """

        self.local_extrema.find(list_with_three_images_3D[1])
        min_index, max_index = self.local_extrema.get_min_max()

        for min_idx in min_index:
            i = min_idx[0]
            j = min_idx[1]
            z = min_idx[2]
            bool_array0 = list_with_three_images_3D[1][i, j, z] < list_with_three_images_3D[0][i - 1:i + 2,
                                                                  j - 1:j + 2, z - 1:z + 2]
            bool_array1 = list_with_three_images_3D[1][i, j, z] < list_with_three_images_3D[2][i - 1:i + 2,
                                                                  j - 1:j + 2, z - 1:z + 2]

            if np.array_equal(bool_array1, bool_array0) and np.array_equal(bool_array0, self.true_array):
                self.min_list.append(min_idx)

        for max_idx in max_index:

            i = max_idx[0]
            j = max_idx[1]
            z = max_idx[2]
            # first image in LoG space comparison
            bool_array0 = list_with_three_images_3D[1][i, j, z] > list_with_three_images_3D[0][i - 1:i + 2,
                                                                  j - 1:j + 2, z - 1:z + 2]
            # third image in LoG space comparison
            bool_array1 = list_with_three_images_3D[1][i, j, z] > list_with_three_images_3D[2][i - 1:i + 2,
                                                                  j - 1:j + 2, z - 1:z + 2]

            if np.array_equal(bool_array1, bool_array0) and np.array_equal(bool_array0, self.true_array):
                self.max_list.append(max_idx)


    def get_min_max(self):
        """
        :return: list of indexes as a np.array min and max [i,j,z]
        """
        return np.array(self.min_list), np.array(self.max_list)



