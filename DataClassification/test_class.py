import gc

__author__ = 'Agnieszka'


import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets, cross_validation

# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features. We could
                      # avoid this ugly slicing by using a two-dim dataset
y = iris.target

  # step size in the mesh

# we create an instance of SVM and fit out data. We do not scale our
# data since we want to plot the support vectors
C = 1.0  # SVM regularization parameter
svc = svm.SVC(kernel='linear', C=C).fit(X, y)
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y)
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, y)
lin_svc = svm.LinearSVC(C=C).fit(X, y)
clf = svm.SVC(kernel='linear', C=1)
svm_metods=[svc,rbf_svc,poly_svc,lin_svc,clf]
scores=[]
for e in svm_metods:
    s=cross_validation.cross_val_score(clf, iris.data, iris.target, cv=5,n_jobs=-1,pre_dispatch='2*n_jobs')
    scores.append(s.mean(),s.std())

plt.figure()
index=np.arange(0,len(s))
plt.errorbar(np.array(s[:][0]), yerr=np.array(s[:][1]),fmt='o')
plt.title("crosvalidation")

