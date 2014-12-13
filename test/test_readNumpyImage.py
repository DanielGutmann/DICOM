from matplotlib.pyplot import imshow, show
from readNumpyImage import ReadNumpyImages

__author__ = 'Agnieszka'

import unittest


class ReadNumpyImagesTest(unittest.TestCase):
    def setUp(self):
        path = './test_data/1_nd/npy_arrays'
        self.ReadImage = ReadNumpyImages(path)
        self.list_of_image = self.ReadImage.open()
    def test_open(self):

        self.assertEqual(len(self.list_of_image),3)
    def test_open_RiseExepction(self):
        try:
            ReadNumpyImages('./test_data/1_nd/').open()
        except IOError:
            pass
        else:
            self.fail('Did not see StopIteration')

    def test_showImage(self):

        for image in self.list_of_image:

            imshow(image,cmap='gray')
            temp=image
            show()




if __name__ == '__main__':
    unittest.main()
