import cv2
import numpy as np

thin_map = [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,
            1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1,
            0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,
            1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1,
            1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,
            1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1,
            0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1,
            1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0,
            1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0]


def erosion(img):
    return cv2.erode(img, np.ones((5, 5), np.uint8), iterations=1)


def dilation(img):
    return cv2.dilate(img, np.ones((5, 5), np.uint8), iterations=1)


def morph_open(img):
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))


def morph_close(img):
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))


def vertical_thin(img, array):
    h, w = img.shape
    NEXT = 1
    for i in range(h):
        for j in range(w):
            if NEXT == 0:
                NEXT = 1
            else:
                M = int(img[i, j-1])+int(img[i, j]) + \
                    int(img[i, j+1]) if 0 < j < w-1 else 1
                if img[i, j] == 0 and M != 0:
                    a = [0]*9
                    for k in range(3):
                        for l in range(3):
                            if -1 < (i-1+k) < h and -1 < (j-1+l) < w and img[i-1+k, j-1+l] == 255:
                                a[k*3+l] = 1
                    sum = a[0]*1+a[1]*2+a[2]*4+a[3]*8 + \
                        a[5]*16+a[6]*32+a[7]*64+a[8]*128
                    img[i, j] = array[sum]*255
                    if array[sum] == 1:
                        NEXT = 0
    return img


def horizontal_thin(img, array):
    h, w = img.shape
    NEXT = 1
    for j in range(w):
        for i in range(h):
            if NEXT == 0:
                NEXT = 1
            else:
                M = int(img[i-1, j])+int(img[i, j]) + \
                    int(img[i+1, j]) if 0 < i < h-1 else 1
                if img[i, j] == 0 and M != 0:
                    a = [0]*9
                    for k in range(3):
                        for l in range(3):
                            if -1 < (i-1+k) < h and -1 < (j-1+l) < w and img[i-1+k, j-1+l] == 255:
                                a[k*3+l] = 1
                    sum = a[0]*1+a[1]*2+a[2]*4+a[3]*8 + \
                        a[5]*16+a[6]*32+a[7]*64+a[8]*128
                    img[i, j] = array[sum]*255
                    if array[sum] == 1:
                        NEXT = 0


def thinning(img, iteration=10):
    for i in range(iteration):
        vertical_thin(img, thin_map)
        horizontal_thin(img, thin_map)
    return img
