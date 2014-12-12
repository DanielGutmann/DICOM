from matplotlib.pyplot import imshow, show

__author__ = 'Agnieszka'

import unittest
from readDicom import ReadDirWithBinaryData
from numpy import array, array_equal


class readDicomTest(unittest.TestCase):
    def setUp(self):
        self.Dicoms = ReadDirWithBinaryData('./test_data/1_nd/')

    def test_get_image3D(self):
        self.assertEqual(self.Dicoms.get_image3D().shape, (512, 512, 74))

    def test_get_spacing(self):
        self.assertEqual(True, array_equal(self.Dicoms.get_spacing(), array([0.9766, 0.9766, 5.0000])))


    def test_readWrongFile(self):
        try:
            ReadDirWithBinaryData('./test_data_error')
        except IOError:
            pass
        else:
            self.fail('Did not see StopIteration')

    def test_showImage(self):
        Z=self.Dicoms.get_image3D()[:, :, 3]
        imshow(Z,cmap='gray')
        show()


if __name__ == '__main__':
    unittest.main()