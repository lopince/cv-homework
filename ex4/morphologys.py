import cv2
import numpy as np


def erosion(img):
    return cv2.erode(img, np.ones((5, 5), np.uint8), iterations=1)


def dilation(img):
    return cv2.dilate(img, np.ones((5, 5), np.uint8), iterations=1)


def morph_open(img):
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))


def morph_close(img):
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))


def thinning(img):
    h, w = img.shape
    iThin = img

    for i in range(h):
        for j in range(w):
            if img[i, j] == 0:
                a = [1] * 9
                for k in range(3):
                    for l in range(3):
                        # 如果3*3矩阵的点不在边界且这些值为零，也就是黑色的点
                        if -1 < (i - 1 + k) < h and -1 < (j - 1 + l) < w and iThin[i - 1 + k, j - 1 + l] == 0:
                            a[k * 3 + l] = 0
                sum = a[0] * 1 + a[1] * 2 + a[2] * 4 + a[3] * 8 + a[5] * 16 + a[6] * 32 + a[7] * 64 + a[8] * 128
                iThin[i, j] = array[sum] * 255
    return iThin

