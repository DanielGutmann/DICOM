from LoGFilter import LoGConvolution3D, LoGConvolution2D
from readDicom import ReadDirWithBinaryData

__author__ = 'Agnieszka'

import unittest


class LoG3DFilterTest(unittest.TestCase):
    def setUp(self):
        mask_size = 40.0
        sigma_zero = 1.6
        octave_size = 5
        self.LoG3DConvolution = LoGConvolution3D(mask_size, sigma_zero, octave_size)
        self.image = ReadDirWithBinaryData('./test_data/1_nd/')

    def test_apply(self):

        self.LoG3DConvolution.apply(self.image)
        #fast_convolution = jit(double[:, :, :](double[:, :, :],
                     #   double[:, :, :]))(self.LoG3DConvolution.apply)
        #fast_convolution(self.image)


class LoG2DFilterTest(unittest.TestCase):
    def setUp(self):
        mask_size = 40.0
        sigma_zero = 1.6
        octave_size = 4
        self.LoG2DConvolution = LoGConvolution2D(mask_size, sigma_zero, octave_size)
        self.image = ReadDirWithBinaryData('./test_data/1_nd/')

    def test_apply(self):
        self.LoG2DConvolution.apply(self.image)


if __name__ == '__main__':
    unittest.main()
