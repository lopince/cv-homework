import cv2


def read(path):
    return cv2.imread(path)


def write(filename, img):
    cv2.imwrite(filename, img)


def toGreyImg(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
