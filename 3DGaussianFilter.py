#from scipy import ndimage

__author__ = 'Agnieszka'
import numpy as np
from scipy.ndimage import  convolve


class GaussianConvolution(object):
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
        self.octaveNo = octaveNo

    def apply(self, Image3D,):
        """
        :param Image3D: image as 3D np.array
        :return: DoG=I(sigma_n)-I(sigma_n-1) difference between smoothed images (I)
        """
        self.gasussian_kernel=#kernel in 3D with size for sigma and size depend on sigma
        ImageForRecurention = convolve(Image3D, self.gaussian_kernel, mode='reflect')

        if(sigma>max): return ImageForRecurention, sigma
        else:
            self.apply(ImageForRecurention)
