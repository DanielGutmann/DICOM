import os

__author__ = 'Agnieszka'
import numpy as np
from os import walk
from os.path import join


class ReadNumpy(object):
    def __init__(self, path):
        self.path = path
        self.ImagesList = []
        self.sigmas_images = []
        self.sigmas_index = []
        self.IndexList = []

    def openImage(self):
        if not os.path.exists(self.path):
            raise IOError
        files_in_dir = [join(self.path, fn) for fn in next(walk(self.path))[2]]
        for f in files_in_dir:
            print(f)
            if '.npy' in f:
                try:
                    file_temp = file(f, 'rb')
                    temp_file = np.load(file_temp)

                    self.ImagesList.append(temp_file['image'])
                    self.sigmas_images.append(temp_file['sigma'])
                finally:
                    file_temp.flush()
                    file_temp.close()
            else:
                raise IOError(f + ' wrong file- probably not npy file')
                return self.ImagesList
        return self.ImagesList
        print('Reading data done')

    def openIndex(self):
        files_in_dir = [join(self.path, fn) for fn in next(walk(self.path))[2]]

        for f in files_in_dir:
            print(f)
            if '.npy' in f:
                try:
                    file_temp = file(f, 'rb')
                    temp_file = np.load(file_temp)
                    self.IndexList.append([temp_file['min'], temp_file['max']])
                    self.sigmas_index.append(temp_file['sigma'])
                finally:
                    file_temp.flush()
                    file_temp.close()
            else:
                raise IOError(f + ' wrong file- probably not npy file')
                return self.ImagesList
        return self.IndexList
        print('Reading data done')

