__author__ = 'Agnieszka'
import cPickle as pickle


class Image3D(object):
    def __init__(self, image3D, spacing, width, high, depth, sigma=0, keypoints_min=0, keypoints_max=0):
        self.Image3D = image3D
        self.spacing = spacing
        self.sigma = sigma
        self.width = width
        self.high = high
        self.depth = depth
        self.keypoints_min = keypoints_min
        self.keypoints_max = keypoints_max

    def get_image3D(self):
        return self.Image3D




