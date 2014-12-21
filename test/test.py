from mayavi.tools.helper_functions import points3d
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numdifftools as nd
from mayavi.mlab import *

x = np.arange(0,60).reshape(5,4,3,order='F')
print x.shape
print(x[:,:,1])
print(x[:,:,2])
xp= np.diff(x,axis=2)
x,y,z= np.gradient(x,3,4,1)
print(xp)
print('___')
print(x)
print('___')
print(y)
print('___')
print(z)
#print np.diff(y,axis=1)
#print np.diff(xp,axis=2)
''''
ReadIndex = ReadNumpy('D:/analiza_danych/DICOM/test/test_data/1_nd/Hessian3D/')
list_with_index = ReadIndex.openIndex()
min_index = list_with_index[0][0]
max_index = list_with_index[2][0]

print len(max_index), len(min_index)

points3d(max_index[:, 0], max_index[:, 1], max_index[:, 2], mode='point')
show()
'''
