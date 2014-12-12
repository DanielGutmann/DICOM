from matplotlib import cm
from numpy import array_equal, min, max

__author__ = 'Agnieszka'

import unittest
from LoGKernel import LoG2D, LoG3D
from matplotlib.pyplot import figure, show


class LoGKernel2DTest(unittest.TestCase):
    def setUp(self):
        sigma = 6.
        self.log = LoG2D(sigma)

    def test_visualization(self):
        fig = figure()
        ax = fig.gca(projection='3d')
        ax.plot_surface(self.log.X, self.log.Y, self.log.get_LoG(), rstride=1, cstride=1, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

        show()

    def test_min_max(self):
        self.assertEqual(abs(min(self.log.x)), (max(self.log.x)))

    def test_min_max_mesh(self):
        self.assertEqual(abs(min(self.log.X)), (max(self.log.X)))
        self.assertEqual(abs(min(self.log.Y)), (max(self.log.Y)))

    def test_kernel_value(self):
        self.kernel = self.log.get_LoG()

        self.assertEqual(True, array_equal(self.kernel[:, 0], self.kernel[:, -1]))
        self.assertEqual(True, array_equal(self.kernel[0, :], self.kernel[-1, :]))
        self.assertEqual(True, array_equal(self.kernel[0, :], self.kernel[:, -1]))


class LoGKernel3DTest(unittest.TestCase):
    def setUp(self):
        sigma = 6
        self.log = LoG3D(sigma)

    def test_min_max(self):
        self.assertEqual(abs(min(self.log.x)), (max(self.log.x)))

    def test_kernel_value(self):
        self.kernel = self.log.get_LoG()
        self.assertEqual(True, array_equal(self.kernel[:, :, 0], self.kernel[:, :, -1]))
        self.assertEqual(True, array_equal(self.kernel[0, :, :], self.kernel[-1, :, :]))
        self.assertEqual(True, array_equal(self.kernel[:, 0, :], self.kernel[:, -1, :]))
