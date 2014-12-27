import math
import numpy
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
        self.rotate.apply(2, 0, 10)
    def test_roatation(self):
        im = self.rotate.apply(2*math.pi, 2*math.pi, 25)
        self.assertEqual(None,assert_array_almost_equal(im,self.open[0].Image3D[246:266, 246:266, 35:39],decimal=16))
        for i in range(0,20):
            for j in range(0,20):
                for z in range(0,4):
                    if(im[i,j,z]!=self.open[0].Image3D[246:266, 246:266, 35:39][i,j,z]):
                        print(im[i,j,z],self.open[0].Image3D[246:266, 246:266, 35:39][i,j,z])




    def test_visualiation(self):
        im,s= self.rotate.apply_for_keypoint(3*math.pi/4,math.pi/2,10, numpy.array([255,255,37]))
        #self.open[0].Image3D = self.open[0].Image3D[246:266, 246:266, 35:39]

        #visualization3D(self.open[0])
        self.open[0].Image3D = im
        self.open[0].spacing=s


        #visualization3D(self.open[0])

        pass


if __name__ == '__main__':
    unittest.main()
