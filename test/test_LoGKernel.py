from matplotlib import cm

__author__ = 'Agnieszka'

import unittest
from LoGKernel import LoG2D
from matplotlib.pyplot import figure, show


class readDicomTest(unittest.TestCase):

    def setUp(self):
        sigma= 60
        self.log=LoG2D(sigma)

    def test_visualization(self):

        fig = figure()
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(self.log.X, self.log.Y, self.log(), rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

        show()
