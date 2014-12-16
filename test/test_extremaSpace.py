
from extramaSpace import ExtremaSpace3D
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'

import unittest


class ExtremaSpace3DTest(unittest.TestCase):
    def setUp(self):
        path = './test_data/1_nd/npy_arrays_3DDoG'
        self.ReadImage = ReadNumpy(path)
        self.list_of_image = self.ReadImage.openImage()
        self.extrema = ExtremaSpace3D(path)

    def test_find(self):

        self.extrema.find(self.list_of_image)




if __name__ == '__main__':
    unittest.main()
