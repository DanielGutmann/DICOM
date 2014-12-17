from numpy import min, max
from keypointOrientation import KeyPointOrientation
from readDicom import ReadDirWithBinaryData
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'
import unittest


class KeyPointOrientationTest(unittest.TestCase):
    def setUp(self):
        self.path = './test_data/1_nd/'
        self.Dicoms = ReadDirWithBinaryData(self.path)
        self.spacing = self.Dicoms.get_spacing()

        self.keypointorientation = KeyPointOrientation(self.spacing, 1)

    def test_pixel_diff(self):
        self.assertEqual(min(self.keypointorientation.pixel_distance_x),
                         -max(self.keypointorientation.pixel_distance_x))
        self.assertEqual(min(self.keypointorientation.pixel_distance_z),
                         -max(self.keypointorientation.pixel_distance_z))

    def test_vectors(self):
        path = './test_data/1_nd/npy_arrays_3DDoG/'
        self.ReadImage = ReadNumpy(path)
        list_of_image = self.ReadImage.openImage()
        self.ReadIndex = ReadNumpy('./test_data/1_nd/npy_arrays_3DDoGmin_maxSpace3D/')
        list_index=self.ReadIndex.openIndex()
        self.keypointorientation = KeyPointOrientation(self.spacing, 1)
        self.keypointorientation.keypoints_histograms(list_index[0][0],list_of_image[1])



if __name__ == '__main__':
    unittest.main()
