from scipy.interpolate import interpn

__author__ = 'Agnieszka'
import numpy as np

m=np.mgrid[0:5,0:5,0:8].T
print m.shape

def _sample_2d_data():
        x = np.arange(0,5)
        #x = np.array([.5, 2., 3., 4., 5.5])
        y = np.arange(0,5)
        #y = np.array([.5, 2., 3., 4., 5.5])
        z = np.ones((5,5,8))
        return x, y, z

x, y, z = _sample_2d_data()
k=np.arange(0,8)
print(z.shape)
#print(x.shape,x)
xi=np.array([[[1,2,2.5,3,3.5,3.9],
                       [1,2,2.5,3,3.5,3.9],[1,2,2.5,3,3.5,3.9]],[[1,2,2.5,3,3.5,3.9],
                       [1,2,2.5,3,3.5,3.9],[1,2,2.5,3,3.5,3.9]],[[1,2,2.5,3,3.5,3.9],
                       [1,2,2.5,3,3.5,3.9],[1,2,2.5,3,3.5,3.9]]]).T
print xi.shape, xi
actual = interpn((x, y,k), z, m)
print np.array([[1, 2.3, 5.3, 0.5, 3.3, 1.2, 3],
                       [1, 3.3, 1.2, 4.0, 5.0, 1.0, 3]]).T
print(actual.T.shape)