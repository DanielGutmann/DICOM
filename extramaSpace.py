from copy import deepcopy
import os
from ReadImage import ReadImage
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

        self.ReadImage = ReadImage(path + '/3DLocalExteremum/')


    def find(self, list_with_images_3D):
        """

        :param list_with_images_3D: list with three images as np.array after LoG in LoG space direction with increasing sigma
        :return: void
        """
        path_to_save = 'DoGSpaceExtremum3D/'

        saving = SavingImageAsNumpy(self.path + path_to_save)
        list_with_im = self.ReadImage.openImage()
        for i in range(1, len(list_with_images_3D)):
            self.min_list = []
            self.max_list = []
            list_with_three_images_3D = list_with_images_3D[i - 1:i + 2]

            min_index = list_with_im[i].keyponits_min
            max_index = list_with_im[i].keyponits_max

            for min_idx in min_index:
                i = min_idx[0]
                j = min_idx[1]
                z = min_idx[2]

                bool_array0 = list_with_three_images_3D[1].Image3D[i, j, z] > list_with_three_images_3D[0].Image3D[
                                                                              i - 1:i + 2,
                                                                              j - 1:j + 2, z - 1:z + 2]
                bool_array1 = list_with_three_images_3D[1].Image3D[i, j, z] > list_with_three_images_3D[2].Image3D[
                                                                              i - 1:i + 2,
                                                                              j - 1:j + 2, z - 1:z + 2]
                sum0 = np.sum(bool_array0) + np.sum(bool_array1)

                if sum0 == 0:
                    self.min_list.append(min_idx)

            for max_idx in max_index:

                i = max_idx[0]
                j = max_idx[1]
                z = max_idx[2]
                # first image in DoG space comparison
                bool_array0 = list_with_three_images_3D[1].Image3D[i, j, z] < list_with_three_images_3D[0].Image3D[
                                                                              i - 1:i + 2,
                                                                              j - 1:j + 2, z - 1:z + 2]
                # third image in DoG space comparison
                bool_array1 = list_with_three_images_3D[1].Image3D[i, j, z] < list_with_three_images_3D[2].Image3D[
                                                                              i - 1:i + 2,
                                                                              j - 1:j + 2, z - 1:z + 2]
                sum0 = np.sum(bool_array0) + np.sum(bool_array1)
                if sum0 == 0:
                    self.max_list.append(max_idx)

            min3D, max3D = self.get_min_max()
            temp_image = deepcopy(list_with_three_images_3D[1])
            temp_image.keypoints_min = min3D
            temp_image.keypoints_max = max3D
            saving.saveImage(temp_image)


    def get_min_max(self):
        """
        :return: list of indexes as a np.array min and max [i,j,z]
        """
        return np.array(self.min_list), np.array(self.max_list)



