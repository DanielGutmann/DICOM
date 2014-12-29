from numpy import zeros
from matrix_for_histogram import matrixHist

__author__ = 'Agnieszka'

import unittest


class matrix_for_histogramTest(unittest.TestCase):
    def setUp(self):
        self.mask = zeros((21, 21, 5))
        self.mask[1:5,3:6,4:]=250
        self.matrixH = matrixHist([.7, .7, 5],15)

    def test_something(self):
        self.matrixH.apply(self.mask)


if __name__ == '__main__':
    unittest.main()
