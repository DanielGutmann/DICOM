__author__ = 'Agnieszka'

import dicom
from os import walk
from os.path import join
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
        return  self.Image3D

class ReadDirWithBinaryData(object):

    def __init__(self, path):
        my_path=path
        np.fromfile(my_path+.)
