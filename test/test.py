from mayavi.tools.helper_functions import points3d
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy
from mayavi.mlab import *

def func(x, y):
    return np.exp(-(x**2+y**2)/2)

grid_x, grid_y = np.mgrid[-1:1:0.1, -1:1:0.1]
points = np.random.rand(1000, 2)*2-1


values = func(points[:,0], points[:,1])

from scipy.interpolate import griddata
print(points.shape,values.shape,grid_x.shape)
grid_z0 = griddata(points, values, (grid_x, grid_y), method='nearest')
grid_z1 = griddata(points, values, (grid_x, grid_y), method='linear')
grid_z2 = griddata(points, values, (grid_x, grid_y), method='cubic')
import matplotlib.pyplot as plt
print(grid_x.shape)
plt.subplot(221)
plt.imshow(func(grid_x, grid_y).T, extent=(-1,1,-1,1), origin='lower')
plt.plot(points[:,0], points[:,1], 'k.', ms=1)
plt.title('Original')
plt.subplot(222)
plt.imshow(grid_z0.T, extent=(-1,1,-1,1), origin='lower')
plt.title('Nearest')
plt.subplot(223)
plt.imshow(grid_z1.T, extent=(-1,1,-1,1), origin='lower')
plt.title('Linear')
plt.subplot(224)
plt.imshow(grid_z2.T, extent=(-1,1,-1,1), origin='lower')
plt.title('Cubic')
plt.gcf().set_size_inches(6, 6)
plt.show()
''''
ReadIndex = ReadNumpy('D:/analiza_danych/DICOM/test/test_data/1_nd/Hessian3D/')
list_with_index = ReadIndex.openIndex()
min_index = list_with_index[0][0]
max_index = list_with_index[2][0]

print len(max_index), len(min_index)

points3d(max_index[:, 0], max_index[:, 1], max_index[:, 2], mode='point')
show()
'''
