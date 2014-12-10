from matplotlib import cm

__author__ = 'Agnieszka'

import unittest
from LoGKernel import LoG2D
from matplotlib.pyplot import figure, show


class readDicomTest(unittest.TestCase):
    def setUp(self):
        sigma = 6
        self.log = LoG2D(sigma)

    def test_visualization(self):
        fig = figure()
        ax = fig.gca(projection='3d')
        ax.plot_surface(self.log.X, self.log.Y, self.log.get_LoG(), rstride=1, cstride=1, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

        show()
