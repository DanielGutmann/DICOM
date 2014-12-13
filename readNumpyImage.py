__author__ = 'Agnieszka'
import numpy as np
from os import walk
from os.path import join


class ReadNumpyImages(object):
    def __init__(self, path):
        self.path = path
        self.ImagesList = []

    def open(self):
        files_in_dir = [join(self.path, fn) for fn in next(walk(self.path))[2]]

        for f in files_in_dir:
            print(f)
            if '.npy' in f:
                try:
                    file_temp = file(f, 'rb')
                    self.ImagesList.append(np.load(file_temp))
                finally:
                    file_temp.flush()
                    file_temp.close()
            else:
                raise IOError(f+' wrong file- probably not npy file')
                return self.ImagesList
        return self.ImagesList
        print('Reading data done')

