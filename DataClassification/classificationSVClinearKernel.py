__author__ = 'Agnieszka'
from DataClassification.FeaturePreprocessor import FeaturePreprocessor

__author__ = 'Agnieszka'

import gc

__author__ = 'Agnieszka'


import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets, cross_validation

path = 'D:/dane/'
feature_preprocessor = FeaturePreprocessor(path)
feature_preprocessor.apply()
data,label=feature_preprocessor.get_data_for_classificator()
# import some data to play with

X = data[:,:-1]
                      # avoid this ugly slicing by using a two-dim dataset
y = data[:,-1]

h = .02  # step size in the mesh

# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
C = 1.0  # SVM regularization parameter
#svc = svm.SVC(kernel='linear', C=C)

# create a mesh to plot in

classificator_list=[]
for i in range (1,10):
    classificator_list.append(svm.SVC(kernel='linear', C=i/10.))
result=[]
if __name__ == '__main__':
    for c in classificator_list:
        temp = cross_validation.cross_val_score(c, X,y, cv=5)
        print(str(c))
        result.append(np.array([temp.mean(),temp.std()]))


result=np.array(result)
print(result)
ex=np.arange(0,len(result))
plt.figure()
plt.errorbar(ex,result[:,0],yerr= result[:,1],fmt='o',)
plt.xlim([-0.5,6])
plt.ylim([-1.3,1.3])
plt.show()


