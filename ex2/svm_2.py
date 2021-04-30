import numpy as np
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as matplot
import os
import seaborn

from tensorflow.examples.tutorials.mnist import input_data
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

os.system('export DISPLAY=:1')

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

start = time.time()

svm = LinearSVC(dual=False)
svm.fit(tr_img, tr_lab)
print "svm.coef_:", svm.coef_
print "svm.intercept_:", svm.intercept_

pred_lab = svm.predict(ts_img)
print("accuracy:", accuracy_score(ts_lab, pred_lab))

print("using:%.2fs" % (time.time()-start))

cm = confusion_matrix(ts_lab, pred_lab)
matplot.subplots(figsize=(10, 6))
seaborn.heatmap(cm, annot=True, fmt='g')
matplot.xlabel('predicted')
matplot.ylabel('Actual')
matplot.title('confusion matrix')
matplot.show()
