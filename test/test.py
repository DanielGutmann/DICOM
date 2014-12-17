from mayavi.tools.helper_functions import points3d
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
I=np.arange(0,16).reshape(4,4)
print I
img_dx = np.diff(I, axis=0)
print img_dx

ReadIndex = ReadNumpy('D:/analiza_danych/DICOM/test/test_data/1_nd/npy_arrays_3DDoGmin_maxSpace3D')
list_with_index = ReadIndex.openIndex()
min_index = list_with_index[2][0]
max_index = list_with_index[2][0]

print len(max_index), len(min_index)

#points3d(max_index[:, 0], max_index[:, 1], max_index[:, 2], mode='point')
#raw_input()

