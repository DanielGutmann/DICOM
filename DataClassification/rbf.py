from DataClassification.FeaturePreprocessorPatient import FeaturePreprocessorPatient

__author__ = 'Agnieszka'
from DataClassification.FeaturePreprocessor import FeaturePreprocessor

__author__ = 'Agnieszka'

import gc

__author__ = 'Agnieszka'

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets, cross_validation

path = 'D:/dane/'
feature_preprocessor = FeaturePreprocessorPatient(path)
feature_preprocessor.apply()
data, label = feature_preprocessor.get_data_for_classificator()
# import some data to play with

X = data[:, :-2]
print(X[1])
p = data[:, -2]  # avoid this ugly slicing by using a two-dim dataset
y = data[:, -1]
print(label)
X = X[y != 6]
y = y[y != 6]

H = np.bincount(y.astype(dtype=np.int8))
ex = np.arange(0, 7)
plt.figure()
width = 1.
plt.bar(ex, H, width=width)
plt.ylabel('liczba wektorow cech dla organu w bazie'.decode('windows-1250'))
plt.xlabel('organ'.decode('windows-1250'))
print label.values()
n=[' ','r','p','b','fL','fR','sm']
plt.xticks(ex + width / 2, n)

plt.xlim([0, 8])
plt.grid(True)
plt.show()

h = .02  # step size in the mesh
# X = X[y != 6]
#y = y[y != 6]
#X = X[y != 3]
#y = y[y != 3]
#X = X[y != 2]
#y = y[y != 2]
print('bez trzech')



# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
C = 1.0  # SVM regularization parameter
# svc = svm.SVC(kernel='linear', C=C)

# create a mesh to plot in

classificator_list = []
#for i in range (0,10):
l = np.array([[0, 0], [1, 1], [1, 1]])
print l.shape
print(X.shape)

c = svm.SVC(C=10, kernel='rbf', gamma=0.5).fit(X, y)

if __name__ == '__main__':
    pass
    temp = cross_validation.cross_val_score(c, X, y, cv=5, n_jobs=4)
    print(temp)
    print(temp.mean(), temp.std())

'''
result=np.array(result)
print(result)
ex=np.arange(0,len(result))
plt.figure()
plt.errorbar(ex,result[:,0],yerr= result[:,1],fmt='o',)
plt.xlim([-0.5,6])
plt.ylim([-1.3,1.3])
plt.show()
'''

