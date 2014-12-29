from matplotlib import cm
from matplotlib.pyplot import figure, show
from numpy import max, linspace, min, meshgrid, array_equal

__author__ = 'Agnieszka'
import unittest
from SizeKernel import SizeKernel2D, SizeKernel3D
from readDicom import ReadDirWithBinaryData


class SizeKernel2DTest(unittest.TestCase):
    def setUp(self):
        spacing = ReadDirWithBinaryData('./test_data/1_nd/').get_spacing()

        self.size_kernel = SizeKernel2D(spacing)
        self.mask_size = 40.
        self.sigma = 6.
        self.kernel = self.size_kernel(self.mask_size, self.sigma)

    def test_plotting(self):
        xx = linspace(min(self.size_kernel.x), max(self.size_kernel.x), self.kernel.shape[0])
        yy = linspace(min(self.size_kernel.y), max(self.size_kernel.y), self.kernel.shape[1])
        grid_x, grid_y = meshgrid(xx, yy)
        fig = figure()
        ax = fig.gca(projection='3d')
        print(self.kernel.shape)
        ax.plot_surface(grid_x, grid_y, self.kernel, rstride=1, cstride=1, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

        show()

    def test_kernel_values(self):

        self.assertEqual(True, array_equal(self.kernel[:, 0], self.kernel[:, -1]))
        self.assertEqual(True, array_equal(self.kernel[0, :], self.kernel[-1, :]))

    def test_kernel_size(self):
        self.assertEqual(self.kernel.shape, (41L, 41L))


class SizeKernel3DTest(unittest.TestCase):
    def setUp(self):
        spacing = ReadDirWithBinaryData('./test_data/1_nd/').get_spacing()

        self.size_kernel = SizeKernel3D(spacing)
        self.mask_size = 40.
        self.sigma = 10.
        self.kernel = self.size_kernel(self.mask_size, self.sigma)


    def test_kernel_values(self):
        self.assertEqual(True, array_equal(self.kernel[:, :, 0], self.kernel[:, :, -1]))
        self.assertEqual(True, array_equal(self.kernel[0, :, :], self.kernel[-1, :, :]))
        self.assertEqual(True, array_equal(self.kernel[:, 0, :], self.kernel[:, -1, :]))

    def test_kernel_size(self):
        self.assertEqual(self.kernel.shape, (41L, 41L,9L))

