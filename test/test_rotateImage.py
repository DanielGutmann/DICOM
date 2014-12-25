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

    def test_visualiation(self):
        im = self.rotate.apply(0, 0, 10)
        self.open[0].Image3D = im
        visualization3D(self.open[0])
        pass


if __name__ == '__main__':
    unittest.main()
