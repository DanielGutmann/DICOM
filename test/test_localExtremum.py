from numpy import array_equal
from localExtermum import LocalExterma3D
from readNumpyImage import ReadNumpyImages

__author__ = 'Agnieszka'

import unittest


class LocalExtrema3DTest(unittest.TestCase):
    def setUp(self):
        path = './test_data/1_nd/npy_arrays'
        self.ReadImage = ReadNumpyImages(path)
        self.list_of_image = self.ReadImage.open()
        self.local_extrema = LocalExterma3D()
        self.image3D_after_log = self.local_extrema.find(self.list_of_image[0])

    def test_true_array(self):
        #self.assertEqual(True, array_equal(self.local_extrema.false_array
        print self.local_extrema.true_array

    def test_get_min_max(self):
        min, max = self.local_extrema.get_min_max()

