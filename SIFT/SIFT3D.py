from GaussianSmoothing import GaussianSmoothing3D
from readDicom import ReadDirWithBinaryData

__author__ = 'Agnieszka'


class SIFT3D(object):
    def __init__(self, path):
        self.path = path

    def apply(self):

        self.Dicoms = ReadDirWithBinaryData(self.path)
        path_analyse = '/CT_analyses/'
        octaves = 6
        initial_sigma = 1.1
        gauss = GaussianSmoothing3D(self.path+path_analyse, octaves).smoothing(initial_sigma)





