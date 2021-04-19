import cv2
import os
import numpy

from PIL import Image


read_dir = os.getcwd() + '/'
write_dir = os.getcwd() + '/res/'

print(read_dir)
print(write_dir)


def read(filename):
    path = read_dir + filename
    print('reading: ', path)
    return cv2.imread(path)


def write(filename, img):
    path = write_dir + filename
    print('writing:', path)
    cv2.imwrite(path, img)


def display(img):
    cv2.imshow(img)


def to_grey_img(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def to_array(img):
    return numpy.array(img)


def from_array(arr):
    return Image.fromarray(arr)
