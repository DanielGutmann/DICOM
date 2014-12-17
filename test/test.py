from mayavi.tools.helper_functions import points3d
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

value_for_extrema=0.0
im=np.ones((3,3,3))
im[1,1,1]=0.0
bool_array = value_for_extrema > im
print(bool_array)
print np.sum(bool_array)

print np.max(np.ones(6))
a = np.random.random(10)
k = 1
t = -1
print k + ((a - np.min(a)) * (t - k) / (np.max(a) - np.min(a)))

ReadIndex = ReadNumpy('D:/analiza_danych/DICOM/test/test_data/1_nd/npy_arrays_3DDoGmin_maxSpace3D')
list_with_index = ReadIndex.openIndex()
min_index = list_with_index[1][0]
max_index = list_with_index[1][0]

print len(max_index)

#points3d(max_index[:, 0], max_index[:, 1], max_index[:, 2], mode='point')
raw_input()


