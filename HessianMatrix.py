__author__ = 'Agnieszka'

import numpy as np


class HessianMatrix(object):
    def __init__(self, threshold, spacing):
        self.threshold = threshold
        self.threshold_sqr = threshold ** 2
        self.keypoints_list = []
        self.spacing = spacing

    def HessianValues(self, Image3D, keypoints):

        img_dx = np.diff(Image3D, axis=0)/self.spacing[0]
        img_dy = np.diff(Image3D, axis=1)/self.spacing[1]
        img_dz = np.diff(Image3D, axis=2)/self.spacing[2]

        img_dxx = np.diff(img_dx, axis=0)/self.spacing[0]
        img_dxy = np.diff(img_dx, axis=1)/self.spacing[1]
        img_dxz = np.diff(img_dx, axis=2)/self.spacing[1]

        img_dyx = np.diff(img_dy, axis=0)/self.spacing[0]
        img_dyy = np.diff(img_dy, axis=1)/self.spacing[1]
        img_dyz = np.diff(img_dy, axis=2)/self.spacing[2]

        img_dzx = np.diff(img_dz, axis=0)/self.spacing[0]
        img_dzy = np.diff(img_dz, axis=1)/self.spacing[1]
        img_dzz = np.diff(img_dz, axis=2)/self.spacing[2]

        for keypoint in keypoints:
            hessian = np.array([img_dxx[keypoint], img_dyx[keypoint], img_dzx[keypoint],
                                img_dxy[keypoint], img_dyy[keypoint], img_dzy[keypoint],
                                img_dxz[keypoint], img_dyz[keypoint], img_dzz[keypoint]])
            Trace = np.trace(hessian)
            Det = np.det(hessian)
            if (Trace ** 3) / Det >= ((2 * self.threshold + 1) ** 3) / self.threshold_sqr:
                self.keypoints_list.append(keypoint)


    def get_key_points(self):
        return np.array(self.keypoints_list)
