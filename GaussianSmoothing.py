from copy import copy, deepcopy
from math import sqrt, ceil
import os
import numpy as np
from skimage.filter import gaussian_filter
from ReadImage import ReadImage
from SaveImage import SaveImage
from SavingNumpyImage import SavingImageAsNumpy
from readDicom import ReadDirWithBinaryData


__author__ = 'Agnieszka'


class GaussianSmoothing2D(object):
    def __init__(self, path, octave_size):
        """

        :param path:path to directory with original images
        :param octave_size: Nos of images in one octave. If it is not odd , it will plus one.

        """
        self.path = path
        self.octave_size = octave_size + octave_size % 2
        self.k = sqrt(2)
        self.image = ReadImage(self.path).openImage()[0]
        self.spacing = self.image.spacing
        self.powers = np.arange(0, self.octave_size)

    def smoothing(self, sigma_zero):
        """
        :param sigma_zero: initial sigma as a first smoothing
        :return:void (images are saved at disc space in path+ '/npy_arrays_2DGaussianFiltering'
        """

        path_to_save = '/2DGaussianSmoothing/'

        sigmas_x = (self.k ** self.powers) * sigma_zero / self.spacing[0]
        sigmas_y = (self.k ** self.powers) * sigma_zero / self.spacing[1]

        # make directory

        im = self.image.Image3D[:, :, 20]
        saving = SaveImage(self.path + path_to_save)
        for sigma_x, sigma_y in zip(sigmas_x, sigmas_y):
            a = -1.
            b = 1.
            max_o = np.max(im)
            min_o = np.min(im)
            image = a + ((im - np.min(im)) * (b - a)) / (np.max(im)) - np.min(im)
            smoothed_image = gaussian_filter(image, (sigma_x, sigma_y))

            image = min_o + ((smoothed_image - np.min(smoothed_image)) * (max_o - min_o)) / (
                np.max(smoothed_image) - np.min(smoothed_image))
            temp_image = deepcopy(self.image)
            temp_image.Image3D = image
            temp_image.sigma = sigma_x

            saving.saveImage(temp_image)


class GaussianSmoothing3D(GaussianSmoothing2D):
    def smoothing(self, sigma_zero):
        """
        :param sigma_zero: initial sigma as a first smoothing
        :return:void (images are saved at disc space in path+ '/npy_arrays_3DGaussianFiltering'
        """
        path_to_save = '/3DGaussianSmoothing/'

        sigmas_x = (self.k ** self.powers) * sigma_zero / self.spacing[0]
        sigmas_y = (self.k ** self.powers) * sigma_zero / self.spacing[1]
        sigmas_z = (self.k ** self.powers) * sigma_zero / self.spacing[2]


        saving = SaveImage(self.path + path_to_save)

        for sigma_x, sigma_y, sigma_z in zip(sigmas_x, sigmas_y, sigmas_z):
            a = -1.
            b = 1.
            im = self.image.Image3D
            max_o = np.max(im)
            min_o = np.min(im)
            image = a + ((im - np.min(im)) * (b - a)) / (np.max(im)) - np.min(im)
            smoothed_image = gaussian_filter(image, (sigma_x, sigma_y, sigma_z))

            smoothed_image = min_o + ((smoothed_image - np.min(smoothed_image)) * (max_o - min_o)) / (
                np.max(smoothed_image) - np.min(smoothed_image))
            temp_image = deepcopy(self.image)
            temp_image.Image3D = smoothed_image

            temp_image.sigma =sigma_x
            saving.saveImage(temp_image)

