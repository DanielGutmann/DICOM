from numpy.random.mtrand import multivariate_normal
from pybrain.datasets            import ClassificationDataSet
from pybrain.utilities           import percentError
from pybrain.tools.shortcuts     import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules   import SoftmaxLayer

from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
import scipy
from scipy.io import savemat
from DataClassification.FeaturePreprocessor import FeaturePreprocessor

path = 'D:/dane/'
feature_preprocessor = FeaturePreprocessor(path)
feature_preprocessor.apply()
data,x=feature_preprocessor.get_data_for_classificator()
#savemat('tets.mat',dict(x=D[:,:-1],y=D[:,-1]))
import numpy as np
import scipy.io

a = np.linspace(0, 2 * np.pi, 100)
b = np.cos(a)
print data[0,0]
#scipy.io.savemat('test.mat', dict(x= data))