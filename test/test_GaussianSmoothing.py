from matplotlib.pyplot import imshow, show
from GaussianSmoothing import GaussianSmoothing3D, GaussianSmoothing2D
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'

import unittest


class Gauss3DTest(unittest.TestCase):
    def setUp(self):
        path = './test_data/1_nd/'
        octaves = 6
        self.gauss = GaussianSmoothing3D(path, octaves)

    def test_soothing(self):
        sigma = 1.1
        self.gauss.smoothing(sigma)

    def test_show(self):
        pass


class Gauss2DTest(unittest.TestCase):
    def setUp(self):
        self.path = './test_data/1_nd/'
        octaves = 6
        self.gauss = GaussianSmoothing2D(self.path, octaves)

    def test_soothing(self):
        sigma = 1.1
        self.gauss.smoothing(sigma)

    def test_show(self):
        path = './test_data/1_nd/npy_arrays_2DGaussianFiltering/'
        self.ReadImage = ReadNumpy(path)
        list_of_image = self.ReadImage.openImage()
        for Z in list_of_image:

            imshow(Z, cmap='gray')
            show()


if __name__ == '__main__':
    unittest.main()
