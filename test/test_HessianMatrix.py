from HessianMatrix import HessianMatrix
from readDicom import ReadDirWithBinaryData
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'

import unittest


class HessianMatrixTest3D(unittest.TestCase):
    def setUp(self):
        self.path = './test_data/1_nd/CT_analyses'
        self.Hessian = HessianMatrix(5.0)

    def test_HessianElimination(self):
        self.Hessian.HessianElimination(self.path)


if __name__ == '__main__':
    unittest.main()
