import cv2


def ostu(grey_img):
    return cv2.threshold(grey_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


def triangle(grey_img):
    return cv2.threshold(grey_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)


def binary(grey_img):
    return cv2.threshold(grey_img, 150, 255, cv2.THRESH_BINARY)


def binary_inv(grey_img):
    return cv2.threshold(grey_img, 150, 255, cv2.THRESH_BINARY_INV)


def trunc(grey_img):
    return cv2.threshold(grey_img, 150, 255, cv2.THRESH_TRUNC)


def tozero(grey_img):
    return cv2.threshold(grey_img, 150, 255, cv2.THRESH_TOZERO)
