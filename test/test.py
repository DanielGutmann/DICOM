from matplotlib import cm
from mayavi.tools.helper_functions import points3d
import scipy
from scipy.ndimage import affine_transform
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numdifftools as nd


''''
m = np.arange(0,27).reshape(3,3,3)


k=np.rot90(m)

src=scipy.misc.lena()
c_in=0.5*np.array(src.shape)
print(c_in)
c_out=np.array((256.0,256.0))
print(c_out)
i=2
a=i*15.0*np.pi/180.0
transform=np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]])
offset=c_in-c_out.dot(transform)
print offset
c_out=np.array([512,512])

x= np.array([0,512]).dot(transform)
y= np.array([512,0]).dot(transform)
print(x,y)
s= np.sqrt(x**2+y**2)
s2=np.abs(x)+np.abs(y)
offset=().dot(transform)

dst=affine_transform(
        src,transform.T,order=2,offset=offset,output_shape=(s2),cval=0.0,output=np.float32
    )
plt.subplot(1,7,i+1);
plt.axis('off');
plt.imshow(dst,cmap=cm.gray)
plt.show()


ReadIndex = ReadNumpy('D:/analiza_danych/DICOM/test/test_data/1_nd/Hessian3D/')
list_with_index = ReadIndex.openIndex()
min_index = list_with_index[0][0]
max_index = list_with_index[2][0]

print len(max_index), len(min_index)

points3d(max_index[:, 0], max_index[:, 1], max_index[:, 2], mode='point')
show()
'''
