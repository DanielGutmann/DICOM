import os
from SavingNumpyImage import SavingImageAsNumpy
from localExtermum import LocalExterma3D
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'
import numpy as np


class ExtremaSpace3D(object):
    def __init__(self, path):
        """
        Find local extrema without edges in LoG space
        """
        self.path = path
        self.min_list = []
        self.max_list = []

        self.ReadIndex = ReadNumpy(path + '/3DLocalExteremum/')


    def find(self, list_with_images_3D):
        """

        :param list_with_images_3D: list with three images as np.array after LoG in LoG space direction with increasing sigma
        :return: void
        """
        path_to_save = 'min_maxSpace3D/'
        try:
            os.makedirs(self.path + path_to_save)
        except OSError:
            pass
        saving = SavingImageAsNumpy(self.path + path_to_save)
        for i in range(1, len(list_with_images_3D) - 1):
            self.min_list = []
            self.max_list = []
            list_with_three_images_3D = list_with_images_3D[i - 1:i + 2]
            list_with_index = self.ReadIndex.openIndex()
            sigma = self.ReadIndex.sigmas_index[i - 1]
            min_index = list_with_index[i - 1][0]
            max_index = list_with_index[i - 1][1]

            for min_idx in min_index:
                i = min_idx[0]
                j = min_idx[1]
                z = min_idx[2]

                bool_array0 = list_with_three_images_3D[1][i, j, z] > list_with_three_images_3D[0][i - 1:i + 2,
                                                                      j - 1:j + 2, z - 1:z + 2]
                bool_array1 = list_with_three_images_3D[1][i, j, z] > list_with_three_images_3D[2][i - 1:i + 2,
                                                                      j - 1:j + 2, z - 1:z + 2]
                sum0 = np.sum(bool_array0) + np.sum(bool_array0)

                if sum0 == 0:
                    self.min_list.append(min_idx)

            for max_idx in max_index:

                i = max_idx[0]
                j = max_idx[1]
                z = max_idx[2]
                # first image in LoG space comparison
                bool_array0 = list_with_three_images_3D[1][i, j, z] < list_with_three_images_3D[0][i - 1:i + 2,
                                                                      j - 1:j + 2, z - 1:z + 2]
                # third image in LoG space comparison
                bool_array1 = list_with_three_images_3D[1][i, j, z] < list_with_three_images_3D[2][i - 1:i + 2,
                                                                      j - 1:j + 2, z - 1:z + 2]
                sum0 = np.sum(bool_array0) + np.sum(bool_array0)
                if sum0 == 0:
                    self.max_list.append(max_idx)

            min3D, max3D = self.get_min_max()
            saving.saveIndex(min3D, max3D, sigma)


    def get_min_max(self):
        """
        :return: list of indexes as a np.array min and max [i,j,z]
        """
        return np.array(self.min_list), np.array(self.max_list)



