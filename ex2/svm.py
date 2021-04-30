from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from tensorflow.examples.tutorials.mnist import input_data
import seaborn
import os
import matplotlib.pyplot as matplot
import numpy as np
import time
import matplotlib
matplotlib.use('Agg')


os.system('export DISPLAY=:0.0')

mnist = input_data.read_data_sets('MNIST_data/')

tr_img = mnist.train.images
val_img = mnist.validation.images
ts_img = mnist.test.images

tr_lab = mnist.train.labels
val_lab = mnist.validation.labels
ts_lab = mnist.test.labels

tr_img = np.concatenate((tr_img, val_img), axis=0)
tr_lab = np.concatenate((tr_lab, val_lab), axis=0)
print('train size:', len(tr_img))
print('test size:', len(ts_img))

for c in [0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000]:

    start = time.time()

    svm = LinearSVC(dual=False, C=c)
    svm.fit(tr_img, tr_lab)
    pred_lab = svm.predict(ts_img)

    print("svm, c=%s, accuracy=%s, using:%.2fs" % (c, accuracy_score(ts_lab, pred_lab), time.time()-start))

# cm = confusion_matrix(ts_lab, pred_lab)
# matplot.subplots(figsize=(10, 6))
# seaborn.heatmap(cm, annot=True, fmt='g')
# matplot.xlabel('predicted')
# matplot.ylabel('Actual')
# matplot.title('confusion matrix')
# matplot.show()
