import os
from SavingNumpyImage import SavingImageAsNumpy
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'


class DoG(object):
    def __init__(self, path, dim):
        self.path = path
        if dim == 2:

            self.open_path = 'npy_arrays_2DGaussianFiltering/'
            try:
                os.makedirs(self.path + 'npy_arrays_2DDoG')
            except OSError:
                pass
            self.path_to_save = '/npy_arrays_2DDoG/'
        elif dim == 3:
            self.open_path = 'npy_arrays_3DGaussianFiltering/'
            try:
                os.makedirs(self.path + 'npy_arrays_3DDoG')
            except OSError:
                pass
            self.path_to_save = 'npy_arrays_3DDoG/'
        else:
            raise (str(dim), "dimension is wrong")

        self.ReadImage = ReadNumpy(self.path + self.open_path)
        # make directory


    def apply(self):
        list_of_image = self.ReadImage.openImage()
        saving = SavingImageAsNumpy(self.path+self.path_to_save)
        for i in range(0, len(list_of_image)-1):
            DoG = list_of_image[i + 1] - list_of_image[i]
            saving.saveImage(DoG,i)