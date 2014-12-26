from math import pi
from numpy import array_equal, sum, rot90
from numpy.testing import assert_array_almost_equal
from ReadImage import ReadImage
from Vizualization import visualization3D
from rotateImage import rotateImage

__author__ = 'Agnieszka'

import unittest


class rotateImageTest(unittest.TestCase):
    def setUp(self):
        self.open = ReadImage('./test_data/1_nd/CT_analyses/KeyPointsOrientation/').openImage()
        self.rotate = rotateImage(self.open[0])

    def test_apply(self):
        self.rotate.apply(0, 0, 10)
    def test_roatation(self):
        im = self.rotate.apply(2*pi, 2*pi, 25)
        self.assertEqual(None,assert_array_almost_equal(im,self.open[0].Image3D[246:266, 246:266, 35:39],decimal=16))
        for i in range(0,20):
            for j in range(0,20):
                for z in range(0,4):
                    if(im[i,j,z]!=self.open[0].Image3D[246:266, 246:266, 35:39][i,j,z]):
                        print(im[i,j,z],self.open[0].Image3D[246:266, 246:266, 35:39][i,j,z])

    def test_roatation90(self):
        im = self.rotate.apply(0,pi/2., 25)
        r=rot90(self.open[0].Image3D[246:266, 246:266, 35:39])
        self.assertEqual(None,assert_array_almost_equal(im,r,decimal=3))
        for i in range(0,20):
            for j in range(0,20):
                for z in range(0,4):
                    if(im[i,j,z]!=self.open[0].Image3D[246:266, 246:266, 35:39][i,j,z]):
                        print(im[i,j,z],self.open[0].Image3D[246:266, 246:266, 35:39][i,j,z])



    def test_visualiation(self):
        im = self.rotate.apply(0, 0, 25)
        self.open[0].Image3D = self.open[0].Image3D[246:266, 246:266, 35:39]
        print(self.open[0].Image3D.shape)
        visualization3D(self.open[0])
        # self.open[0].Image3D = im
        print(im.shape)
        #visualization3D(self.open[0])
        pass


if __name__ == '__main__':
    unittest.main()
