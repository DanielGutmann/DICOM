from ResizeImage import ResizeImage2D, ResizeImage3D
from readDicom import ReadDirWithBinaryData

__author__ = 'Agnieszka'
import unittest


class ResizeImage2DTest(unittest.TestCase):
    def setUp(self):
        self.image = ReadDirWithBinaryData('./test_data/1_nd/').get_image3D()[:, :, 20]
        self.resize = ResizeImage2D()
        self.resize_img = self.resize.apply(self.image)

    def test_size(self):
        self.assertEqual(self.resize_img.shape, (256L, 256L))


class ResizeImage3DTest(unittest.TestCase):
    def setUp(self):
        self.image = ReadDirWithBinaryData('./test_data/1_nd/').get_image3D()
        self.resize = ResizeImage3D()
        self.resize_img = self.resize.apply(self.image)

    def test_size(self):
        self.assertEqual(self.resize_img.shape, (256L, 256L, 37L))

