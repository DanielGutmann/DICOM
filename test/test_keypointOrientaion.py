from math import pi
from mayavi.tools.helper_functions import quiver3d
from mayavi.tools.show import show
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
        path = './test_data/1_nd/npy_arrays_3DDoG/'
        self.ReadImage = ReadNumpy(path)
        self.list_of_image = self.ReadImage.openImage()
        self.ReadIndex = ReadNumpy('./test_data/1_nd/npy_arrays_3DDoGmin_maxSpace3D/')
        self.list_index = self.ReadIndex.openIndex()

    def test_pixel_diff(self):
        self.assertEqual(min(self.keypointorientation.pixel_distance_x),
                         -max(self.keypointorientation.pixel_distance_x))
        self.assertEqual(min(self.keypointorientation.pixel_distance_z),
                         -max(self.keypointorientation.pixel_distance_z))

    def test_vectors(self):
        self.keypointorientation = KeyPointOrientation(self.spacing, 1)
        self.keypointorientation.keypoints_histograms(self.list_index[0][0], self.list_of_image[1])

    def test_weights_vizualization(self):
        self.keypointorientation = KeyPointOrientation(self.spacing, 1.1)
        self.keypointorientation.keypoints_histograms(self.list_index[0][0], self.list_of_image[1])
        u = self.keypointorientation.azimuth
        v = self.keypointorientation.elevation
        w = self.keypointorientation.weights
        print max(w),min(w),pi
        #obj = quiver3d(w,u, v, line_width=3, scale_factor=1)
        #show()


if __name__ == '__main__':
    unittest.main()
