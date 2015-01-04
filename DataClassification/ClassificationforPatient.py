from DataClassification.FeaturePreprocessorPatient import FeaturePreprocessorPatient

__author__ = 'Agnieszka'

from sklearn import svm, datasets, cross_validation
import numpy as np
path = 'D:/dane/'
feature_preprocessor = FeaturePreprocessorPatient(path)
feature_preprocessor.apply()
data, label = feature_preprocessor.get_data_for_classificator()
# import some data to play with

X = data[:, :-2]

p = data[:, -2]  # avoid this ugly slicing by using a two-dim dataset
y = data[:, -1]
print(np.histogram(y, bins=6))
  # step size in the mesh
'''
X = X[y != 6]
y = y[y != 6]
X = X[y != 3]
y = y[y != 3]
X = X[y != 2]
y = y[y != 2]
'''
print('bez trzech')
f = open('workfile', 'w')
for i in range(1, 42):

    f.write('Pacjent nr: '+str(i)+'\n')
    X_t = X[p == i]
    y_t = y[p == i]
    if(X_t.size==0):
        continue
    X_n = X[p != i]
    y_n = y[p != i]
    clf = svm.SVC(kernel='rbf', gamma=0.1).fit(X_n, y_n)

    f.write(str(clf.score(X_t, y_t))+'\n')

    for i in range(1,7):

        f.write(str(label[i])+' '+str(clf.score(X_t[y_t==i],y_t[y_t==i]))+'\n')

    f.write('\n')
