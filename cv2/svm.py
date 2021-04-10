import os
import numpy as np

from time import time
from struct import unpack
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV


def load_images(path):
    with open(path, 'rb') as f:
        magic, num, rows, cols = unpack('>4I', f.read(16))
        images = np.fromfile(f, dtype=np.uint8).reshape(num, 784)
    return images


def load_labels(path):
    with open(path, 'rb') as f:
        magic, num = unpack('>2I', f.read(8))
        lab = np.fromfile(f, dtype=np.uint8)
    return lab


train_images = load_images('./train-images-idx3-ubyte')
train_labels = load_labels('./train-labels-idx1-ubyte')

test_images = load_images('./t10k-images-idx3-ubyte')
test_labels = load_labels('./t10k-labels-idx1-ubyte')

svc = SVC()
params = {}
params['kernel'] = ['rbf']
params['C'] = [1]

start_time = time()
gs = GridSearchCV(svc, params, n_jobs=-1)
gs.fit(train_images, train_labels)
print('trained, time consuming: {}s'.format(time()-start_time))
