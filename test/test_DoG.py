import unittest
from matplotlib.pyplot import imshow, show
import numpy
from DoG import DoG
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'


class DoG2DTest(unittest.TestCase):
    def setUp(self):
        self.path = './test_data/1_nd/'
        self.dog = DoG(self.path, 2)

    def test_soothing(self):
        self.dog.apply()


    def test_show(self):
        path = './test_data/1_nd/npy_arrays_2DDoG/'
        self.ReadImage = ReadNumpy(path)
        list_of_image = self.ReadImage.openImage()
        for Z in list_of_image:
            print numpy.min(Z), numpy.max(Z)
            imshow(Z, cmap='gray')
            show()


class DoG3DTest(unittest.TestCase):
    def setUp(self):
        self.path = './test_data/1_nd/'
        self.dog = DoG(self.path, 3)

    def test_soothing(self):
        self.dog.apply()

    def test_show(self):
        path = './test_data/1_nd/npy_arrays_3DDoG/'
        self.ReadImage = ReadNumpy(path)
        list_of_image = self.ReadImage.openImage()


if __name__ == '__main__':
    unittest.main()
