import numpy as np
from scipy.signal import argrelextrema

from multiprocessing import Process, Array

def f(list,a):
    lista=list
    for i in range(len(a)):
        for j in range(len(a)):
            for z in range(len(a)):
                a[i,j,z] = -a[i]

if __name__ == '__main__':

    arr = Array('i', range((10,10,3)))

    p = Process(target=f, args=(arr))
    p.start()
    p.join()


    print arr[:]

from joblib import Parallel, delayed
import multiprocessing

# what are your inputs, and what operation do you want to
# perform on each input. For example...
inputs = range(10)
def processInput(i):
    return i * i

num_cores = multiprocessing.cpu_count()

results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in inputs)