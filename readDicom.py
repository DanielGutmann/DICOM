__author__ = 'Agnieszka'

from os import walk
from os.path import join

import dicom
import numpy as np


class ReadDirWithDicom(object):
    def __init__(self, path):

        my_path = path
        files_in_dir = [join(my_path, fn) for fn in next(walk(my_path))[2]]
        image3D = []
        for f in files_in_dir:
            if ".IMA" in f:
                dicom_data_set = dicom.read_file(f)
                image3D.append(dicom_data_set.pixel_array)
            else:
                raise IOError('wrong file- probably not DICOM')
        self.Image3D = np.dstack(image3D)
        print('Reading data done')


    def get_all_slices_in_3D(self):
        return self.Image3D


class ReadDirWithBinaryData(object):
    def __init__(self, path):
        self.my_path = path
        self.mata_bin = open(self.my_path + 'hdr_CT.bin.txt')
        self.width = int(self.mata_bin.readline().split(' = ')[1][:-2])
        self.hight = int(self.mata_bin.readline().split(' = ')[1][:-2])
        self.depth = int(self.mata_bin.readline().split(' = ')[1][:-2])
        self.data_type = self.mata_bin.readline().split(' = ')[1][:-2]
        l = open(self.my_path + 'CT.bin', "r")
        f = (np.array(np.fromfile(l, dtype="<f4")))

        self.Image3D = np.reshape(f,
                                  (self.width, self.hight, 74 ), order='F')

        if np.max(self.Image3D) < 0.1:
            self.Image3D = self.Image3D.byteswap()
        self.spaceing = np.fromfile(self.my_path + 'spacing.txt', dtype=self.data_type, sep="    ")
        print('Reading data done')

    def get_image3D(self):
        return self.Image3D

    def get_spacing(self):
        return self.spaceing