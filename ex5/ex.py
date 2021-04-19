import binarizes
import imgs


def add_noise(img):
    

img = imgs.read('test.jpg')
grey_img = imgs.toGreyImg
binary_img = binarizes.binary(img)

