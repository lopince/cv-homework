import numpy as np

from PIL import Image


def median(img, k=3):

    img_arr = np.array(img)
    h, w = img_arr.shape

    edge = int((k-1)/2)
    temp_arr = np.zeros((h, w), dtype="uint8")

    for i in range(h):
        for j in range(w):
            if i <= edge - 1 or i >= h - 1 - edge or j <= edge - 1 or j >= h - edge - 1:
                temp_arr[i, j] = img_arr[i, j]
            else:
                neighbor_mat = img_arr[i - edge:i + edge + 1, j - edge:j + edge + 1]
                max = np.max(neighbor_mat)
                min = np.min(neighbor_mat)
                if img_arr[i, j] == max or img_arr[i, j] == min:
                    temp_arr[i, j] = np.median(neighbor_mat)
                else:
                    temp_arr[i, j] = img_arr[i, j]

    return Image.fromarray(temp_arr)
