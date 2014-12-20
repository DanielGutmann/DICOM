import os
from ReadImage import ReadImage
from SaveImage import SaveImage
from SavingNumpyImage import SavingImageAsNumpy
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'

import numpy as np


class HessianMatrix(object):
    def __init__(self, threshold):
        self.threshold = threshold
        self.threshold_sqr = threshold ** 2
        self.keypoints_list = []
        self.spacing = 0


    def HessianValues(self, image, keypoints):
        self.keypoints_list = []
        Image3D = image.Image3D
        self.spacing = image.spacing
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

        return self.get_key_points()

    def HessianElimination(self, path):
        """
        :param path: path to CT analyses folder
        :return:void saving images aggregator
        """

        path = path
        path_to_save = '/Hessian3D/'

        saving = SaveImage(path + path_to_save)
        ReadIm = ReadImage(path + '/3DDoG/DoDSpaceExtremum3D/')
        im = ReadIm.openImage()

        for i in range(0, len(im)):
            if im[i].keypoints_min.shape[0] != 0:
                im[i].keypoints_min = self.HessianValues(im[i], im[i].keypoints_min)

            if im[i].keypoints_max.shape[0] != 0:
                im[i].keypoints_max = self.HessianValues(im[i], im[i].keypoints_max)

            saving.saveImage(im)

    def get_key_points(self):
        return np.array(self.keypoints_list)
