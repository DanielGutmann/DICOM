import os
from SavingNumpyImage import SavingImageAsNumpy
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'

import numpy as np


class HessianMatrix(object):
    def __init__(self, threshold, spacing):
        self.threshold = threshold
        self.threshold_sqr = threshold ** 2
        self.keypoints_list = []
        self.spacing = spacing

    def HessianValues(self, Image3D, keypoints):
        self.keypoints_list = []
        img_dx = np.diff(Image3D, axis=0) / self.spacing[0]
        img_dy = np.diff(Image3D, axis=1) / self.spacing[1]
        img_dz = np.diff(Image3D, axis=2) / self.spacing[2]

        img_dxx = np.diff(img_dx, axis=0) / self.spacing[0]
        img_dxy = np.diff(img_dx, axis=1) / self.spacing[1]
        img_dxz = np.diff(img_dx, axis=2) / self.spacing[1]

        img_dyx = np.diff(img_dy, axis=0) / self.spacing[0]
        img_dyy = np.diff(img_dy, axis=1) / self.spacing[1]
        img_dyz = np.diff(img_dy, axis=2) / self.spacing[2]

        img_dzx = np.diff(img_dz, axis=0) / self.spacing[0]
        img_dzy = np.diff(img_dz, axis=1) / self.spacing[1]
        img_dzz = np.diff(img_dz, axis=2) / self.spacing[2]

        for keypoint in keypoints:
            i = keypoint[0]
            j = keypoint[1]
            z = keypoint[2]
            try:
                hessian = np.array([[img_dxx[i, j, z], img_dyx[i, j, z], img_dzx[i, j, z]],
                                    [img_dxy[i, j, z], img_dyy[i, j, z], img_dzy[i, j, z]],
                                    [img_dxz[i, j, z], img_dyz[i, j, z], img_dzz[i, j, z]]])
                Trace = np.trace(hessian)
                Det = np.linalg.det(hessian)
                det_p_2 = img_dxx[i, j, z] * img_dzz[i, j, z] - img_dyz[i, j, z] ** 2 + img_dxx[i, j, z] * img_dzz[
                    i, j, z] - img_dzz[i, j, z] ** 2 + img_dxx[i, j, z] * img_dyy[i, j, z] - img_dxy[i, j, z] ** 2
                if Det != 0.0:
                    if (Trace ** 3) / Det < ((2 * self.threshold + 1) ** 3) / self.threshold_sqr:
                        if Trace * Det > 0:
                            if det_p_2 > 0:
                                self.keypoints_list.append(keypoint)

            except IndexError:

                pass

        return self.keypoints_list

    def HessianElimination(self, path, list_with_images):

        path = path

        path_to_save = 'Hessian3D/'
        try:
            os.makedirs(path + path_to_save)
        except OSError:
            pass
        saving = SavingImageAsNumpy(path + path_to_save)
        ReadIndex = ReadNumpy(path + '/npy_arrays_3DDoGmin_maxSpace3D/')
        index = ReadIndex.openIndex()


        sigmas = ReadIndex.sigmas_index
        for i in range(1, len(list_with_images)-1):

            min3D = self.HessianValues(list_with_images[i], index[i-1][0])
            max3D = self.HessianValues(list_with_images[i], index[i-1][1])
            saving.saveIndex(min3D, max3D, sigmas[i-1])

    def get_key_points(self):
        return np.array(self.keypoints_list)
