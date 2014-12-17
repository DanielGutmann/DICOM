from HessianMatrix import HessianMatrix
from readDicom import ReadDirWithBinaryData
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'

import unittest


class HessianMatrixTest3D(unittest.TestCase):
    def setUp(self):
        self.path='./test_data/1_nd/'
        self.Dicoms = ReadDirWithBinaryData(self.path)
        spacing=self.Dicoms.get_spacing()

        self.Hessian = HessianMatrix(5.0, spacing)

    def test_HessianElimination(self):
        path = './test_data/1_nd/npy_arrays_3DDoG/'
        self.ReadImage = ReadNumpy(path)
        list_of_image = self.ReadImage.openImage()
        self.Hessian.HessianElimination(self.path,list_of_image)


if __name__ == '__main__':
    unittest.main()
