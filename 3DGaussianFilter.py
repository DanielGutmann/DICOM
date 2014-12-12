# from scipy import ndimage
from tempfile import TemporaryFile
from SizeKernel import SizeKernel3D

__author__ = 'Agnieszka'
import numpy as np
from scipy.ndimage import convolve


class LoGConvolution(object):
    '''
    Gaussian convolution for one 3D image as np.array
    '''


    def __init__(self, mask_size, sigma_zero, octave_size, octaveNo):
        """
        :param mask_size: size of kernel
        :param sigma_zero: initial value of sigma for first smoothing
        :param octave_size: number of smoothed images in octave
        :param octaveNo: number of octave (maximal subsumplig 4*octaveNo)
        :return: void
        """
        self.mask_size = mask_size
        self.sigma_zero = sigma_zero
        self.octave_size = octave_size


    def apply(self, Image3D_with_spacing):
        """
        :param Image3D_with_spacing: object ReadDirWithBinaryData
        :return: I(sigma_n)=LoG(sigma)*Image
        """

        size_kernel = SizeKernel3D(Image3D_with_spacing.get_spacing())
        sigma = self.sigma_zero
        kernel = size_kernel(self.mask_size, sigma)
        Image_after_convolution = np.convolve(Image3D_with_spacing.get_image3D(), kernel)
        sigmas=[self.sigma_zero]
        size=0
        for sigma in sigmas:
            kernel = size_kernel(self.mask_size, sigma)
            Image_after_convolution = np.convolve(Image_after_convolution, kernel)
            outfile = file(Image3D_with_spacing.my_path+'_'+str(sigma))
            np.savez(outfile,Image_after_convolution)