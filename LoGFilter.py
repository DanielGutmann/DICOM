# from scipy import ndimage
from math import sqrt
from tempfile import TemporaryFile
from numba import jit
from SizeKernel import SizeKernel3D, SizeKernel2D

__author__ = 'Agnieszka'
import numpy as np
from scipy.ndimage import convolve


class LoGConvolution2D(object):
    """
    Gaussian convolution for one 3D image as np.array
    """


    def __init__(self, mask_size, sigma_zero, octave_size):
        """
        :param mask_size: size of kernel
        :param sigma_zero: initial value of sigma for first smoothing
        :param octave_size: number of smoothed images in octave

        :return: void
        """
        self.mask_size = mask_size
        self.sigma_zero = sigma_zero
        self.octave_size = octave_size


    def apply(self, image2D_with_spacing):
        """
        :param image3D_with_spacing: object ReadDirWithBinaryData
        :return: I(sigma_n)=LoG(sigma)*Image
        """
        print('object creation')
        size_kernel = SizeKernel2D(image2D_with_spacing.get_spacing())

        image_after_convolution= image2D_with_spacing.get_image3D()[:, :, 1]
        sig = np.linspace(self.sigma_zero, self.sigma_zero * 2, self.octave_size)
        #print(sig)

        #temp = np.sqrt(sig[1:] ** 2 - sig[:-1] ** 2)
        #sig[1:] = temp
        #print(sig)
        print('object creation end')
        for sigma in sig:
            print('kernel creation')
            kernel = size_kernel(self.mask_size, sigma)
            print('object creation end')
            print 'convolution start'
            image_after_convolution = convolve(image_after_convolution, kernel)/np.sum(kernel)
            print('convolution end')

            outfile = file(image2D_with_spacing.my_path + 'npy_arrays/2D_' + str(sigma)+'.npy', 'wb')
            print('file is saving')
            np.save(outfile, image_after_convolution)

            outfile.flush()
            outfile.close()

            print('file saved')


class LoGConvolution3D(object):
    """
    Gaussian convolution for one 3D image as np.array
    """


    def __init__(self, mask_size, sigma_zero, octave_size):
        """
        :param mask_size: size of kernel
        :param sigma_zero: initial value of sigma for first smoothing
        :param octave_size: number of smoothed images in octave

        :return: void
        """
        self.mask_size = mask_size
        self.sigma_zero = sigma_zero
        self.octave_size = octave_size


    def apply(self, image3D_with_spacing):
        """
        :param image3D_with_spacing: object ReadDirWithBinaryData
        :return: I(sigma_n)=LoG(sigma)*Image
        """
        print('object creation')
        size_kernel = SizeKernel3D(image3D_with_spacing.get_spacing())

        image_after_convolution = image3D_with_spacing.get_image3D()
        sig = np.linspace(self.sigma_zero, self.sigma_zero * 2, self.octave_size)
        print(sig)

        #temp = np.sqrt(sig[1:] ** 2 - sig[:-1] ** 2)
        #sig[1:] = temp

        print('object creation end')

        for sigma in sig:
            print('kernel creation')
            kernel = size_kernel(self.mask_size, sigma)
            print('object creation end')
            print 'convolution start'
            image_after_convolution = convolve(image_after_convolution, kernel)
            print('convolution end')


            outfile = file(image3D_with_spacing.my_path + 'npy_arrays_3d/3D_' + str(sigma) + '.npy', 'wb')
            print('file is saving')

            np.save(outfile, image_after_convolution)
            outfile.flush()
            outfile.close()
            print('file saved')
