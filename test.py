__author__ = 'Agnieszka'
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.linalg import misc
from scipy.stats import stats, norm
from scipy import misc , ndimage
from math import pi, sqrt
from numpy import exp
import numpy as np
from skimage.filter import gaussian_filter
from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
from readDicom import ReadDirWithBinaryData

fig = plt.figure()
ax = fig.gca(projection='3d')
zer=np.zeros((3,3))
zer[1,1]=1.0
im = fig.add_subplot(1, 2, 2)
print zer
l=ndimage.filters.gaussian_laplace(zer,1,mode='constant')
print(l)
k= l/np.sum(l)
print np.sum(k)
im.imshow(k,cmap = cm.Greys_r,interpolation='none' )
plt.show()

ax = fig.add_subplot(1, 2, 1, projection='3d')

x = np.arange(-21, 21, 1)
y = np.arange(-20, 21, 1)
z = np.arange(-20, 21, 0.5)
sigmas =np.linspace(1.6, 24., 15)
print x.shape
xx, yy ,zz = np.meshgrid(x, y,z)
xx2, yy2 = np.meshgrid(x, y)
cubic=xx**2 + yy**2+zz**2
pow=xx2**2 + yy2**2



sigma=10
z2= -((1/((sigma**4)*pi))*(1-(pow/(2*(sigma**2)))))*np.exp(-pow / (2*sigma**2))

#z2=z -((1/((sigma**4)*pi))*(1-(cubic/(2*(sigma**2)))))*np.exp(-cubic / (2*sigma**2))
t=ax.plot_surface(xx2, yy2, z2,rstride=1, cstride=1, cmap=cm.coolwarm,
       linewidth=0, antialiased=False)
lena=misc.lena()

lena=ndimage.filters.convolve(lena,z2)
lena=lena/np.sum(z2)
im.imshow(lena,cmap = cm.Greys_r)
plt.show()
plt.show(t)
plt.show()