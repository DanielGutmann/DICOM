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
X = X[y != 6]
y = y[y != 6]

h = .02  # step size in the mesh

# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
C = 1.0  # SVM regularization parameter
svc = svm.SVC(kernel='linear', C=C)
print('svc')
rbf_svc = svm.SVC(kernel='rbf', gamma=0.1, C=C)
print('rbf')
poly_svc = svm.SVC(kernel='poly', degree=3, C=C)
print('poly')
lin_svc = svm.LinearSVC(C=C)
print('lin')

# create a mesh to plot in

c=[rbf_svc]
result=[]
if __name__ == '__main__':
        temp = cross_validation.cross_val_score(c[0], X,y, cv=10,n_jobs=4)
        print(temp.mean(),temp.std())





