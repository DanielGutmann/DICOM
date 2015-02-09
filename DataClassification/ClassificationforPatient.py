from sklearn.neighbors import NearestNeighbors, KNeighborsClassifier
from DataClassification.FeaturePreprocessorPatient import FeaturePreprocessorPatient
from pointsPixelFeature import pointsPixelFeature

__author__ = 'Agnieszka'

from sklearn import svm, datasets, cross_validation
import numpy as np
path = 'D:/dane/'
feature_preprocessor =  pointsPixelFeature(path)
#feature_preprocessor=FeaturePreprocessorPatient(path)
feature_preprocessor.apply()
data, label = feature_preprocessor.get_data_for_classificator()
# import some data to play with

X = data[:, :-2]
print(X.shape)
p = data[:, -2]  # avoid this ugly slicing by using a two-dim dataset
y = data[:, -1]

print((np.bincount(p.astype(dtype=np.int16))!=0).sum())
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
f = open('workfile_pixel_25_anizotropy', 'w')
for i in range(1, 43):

    f.write('Pacjent nr: '+str(i)+'\n')
    X_t = X[p == i]
    y_t = y[p == i]
    if(X_t.size==0):
        continue
    X_n = X[p != i]
    y_n = y[p != i]
    #clf = svm.SVC(kernel='rbf', gamma=0.1).fit(X_n, y_n)
    clf = KNeighborsClassifier(n_neighbors=6,weights='distance')._fit(X_n,y_n)
    f.write(str(clf.score(X_t, y_t))+'\n')

    for i in range(1,7):
        #(clf.predict(X_t[y_t==i])==i).sum()/X_t[y_t==i].size
        f.write(str(label[i])+' '+str(clf.score(X_t[y_t==i],y_t[y_t==i]))+'\n')

    f.write('\n')
