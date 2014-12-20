from ReadImage import ReadImage
from Vizualization import keypoints_vizualization
from extramaSpace import ExtremaSpace3D
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'

import unittest


class ExtremaSpace3DTest(unittest.TestCase):
    def setUp(self):
        path = './test_data/1_nd/3DDoG'
        self.ReadImage = ReadImage(path)
        self.list_of_image = self.ReadImage.openImage()
        self.extrema = ExtremaSpace3D(path)

    def test_find(self):

        self.extrema.find(self.list_of_image)

    def test_show(self):
        path = './test_data/1_nd/CT_analyses/3DDoG/3DSpaceExtremum/'
        list_with_images = ReadImage(path).openImage()
        for z in list_with_images:
            keypoints_vizualization(z)



if __name__ == '__main__':
    unittest.main()
