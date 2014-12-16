import numpy as np
from scipy.signal import argrelextrema

from multiprocessing import Process, Pool
from readNumpyImage import ReadNumpy

class f(object):



    def find(image3D, i):
            """

            :param image3D: image after convolution LoG
            :return: void
            """
            true_array = np.ones((3, 3, 3), dtype=np.bool)
            true_array[1, 1, 1] = False
            false_array = -true_array
            min_list = []
            max_list = []
            shape = image3D.shape
            #outputmin = mp.Queue()
            #outputmax = mp.Queue()

            for j in range(1, shape[1]):
                    for z in range(1, shape[2]):
                        value_for_extrema = image3D[i, j, z]
                        bool_array = value_for_extrema < image3D[i - 1:i + 2, j - 1:j + 2, z - 1:z + 2]

                        if np.array_equal(bool_array, true_array):
                            return  (np.array([i, j, z]))
                        elif np.array_equal(bool_array, false_array):
                            return (np.array([i, j, z]))


if __name__ == '__main__':
        pool = Pool(processes=4)

        path = 'D:/analiza_danych/DICOM/test/test_data/1_nd/npy_arrays_3d'
        f1=f()
        ReadImage = ReadNumpy(path)
        list_of_image = ReadImage.open()



        min1 = [pool.apply(f.find, args=(list_of_image[0],i,))  for i in range(1, 512)]



