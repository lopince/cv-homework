import cv2
import os


dir = os.getcwd() + '/ex4/'


def read(filename):
    print('reading: ', dir + filename)
    return cv2.imread(dir + filename)


def write(filename, img):
    cv2.imwrite(dir + filename, img)


def display(img):
    cv2.imshow(img)


def toGreyImg(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
