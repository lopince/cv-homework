import binarizes
import imgs
import numpy as np
import filters


def add_noise(img, snr=0.9):
    img_arr = imgs.to_array(img)
    print(type(img))
    h, w = img_arr.shape
    temp_arr = img_arr.copy()
    sp = h * w
    NP = int(sp * (1 - snr))
    for i in range(NP):
        x = np.random.randint(1, h - 1)
        y = np.random.randint(1, w - 1)
        if np.random.random() <= 0.5:
            temp_arr[x, y] = 0
        else:
            temp_arr[x, y] = 255

    return np.asarray(temp_arr)


img = imgs.read('test.jpg')
grey_img = imgs.to_grey_img(img)
binary_img = binarizes.binary(grey_img)[1]
imgs.write('binary.jpg', binary_img)

noised_img = add_noise(binary_img)
print(type(noised_img))
imgs.write('noised.jpg', noised_img)

median_filtered_img = filters.median(noised_img)
imgs.write('median_filtered.jpg', median_filtered_img)
