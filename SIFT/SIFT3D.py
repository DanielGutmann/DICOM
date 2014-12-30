from DoG import DoG
from GaussianSmoothing import GaussianSmoothing3D
from OpenMask import OpenMask
from localExtermum import LocalExterma3D
from readDicom import ReadDirWithBinaryData

__author__ = 'Agnieszka'


class SIFT3D(object):
    def __init__(self, path):
        self.path = path

    def apply(self):
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
        local_extrema = LocalExterma3D(self.path+pathDoG, self.path+path_analyse, True)
        local_extrema.find()






