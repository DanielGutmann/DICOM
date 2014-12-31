from DoG import DoG
from GaussianSmoothing import GaussianSmoothing3D
from HessianMatrix import HessianMatrix
from OpenMask import OpenMask
from ReadImage import ReadImage
from extramaSpace import ExtremaSpace3D
from images_features import KeypointsFeatures
from keypointOrientation import KeyPointOrientation
from localExtermum import LocalExterma3D
from readDicom import ReadDirWithBinaryData
from rotateImage import rotateImage

__author__ = 'Agnieszka'


class SIFT3D(object):
    def __init__(self, path):
        self.path = path

    def apply(self):
        #first scale
        self.Dicoms = ReadDirWithBinaryData(self.path)
        mask = OpenMask(self.path)
        path_analyse = '/CT_analyses/'
        octaves = 6
        initial_sigma = 1.1
        gauss = GaussianSmoothing3D(self.path + path_analyse, octaves).smoothing(initial_sigma)
        dimension = 3
        dog = DoG(self.path + path_analyse, dimension)
        dog.apply()
        pathDoG = '/CT_analyses/3DDoG/'
        local_extrema = LocalExterma3D(self.path + pathDoG, self.path + path_analyse, True)
        local_extrema.find()
        path_local_extrema = '/3DLocalExtremum/'
        extrema = ExtremaSpace3D(self.path + pathDoG + path_local_extrema)
        extrema.find()
        Hessian = HessianMatrix(40.0)
        Hessian.HessianElimination(self.path + path_analyse)
        keypointorientation = KeyPointOrientation(self.path + path_analyse)
        keypointorientation.apply()
        path_keypoint_orientation = '/KeyPointsOrientation/'
        images = ReadImage(self.path + path_analyse + path_keypoint_orientation).openImage()
        for im in images:
            rotateImage(im, 10, self.path + path_analyse)

        path_discriptor = '/Descriptor3D/'
        keydis=KeypointsFeatures(self.path + path_analyse+path_discriptor, self.path + path_analyse)


    def test_something(self):
        self.keydis.apply()


    def test_apply(self):
        import time

        c = time.clock()
        self.rotate.apply()
        print(c - time.clock())






