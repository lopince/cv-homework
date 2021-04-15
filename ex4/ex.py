import imgs
import binarizes


# 读取图片
img = imgs.read('test.jpg')

# 转化为灰度图
grey_img = imgs.toGreyImg(img)

# 二值化

# 大津法—最大类间方差法
thr, binary = binarizes.ostu(grey_img)
print('ostu threshold:', thr)

# triangle
thr, binary = binarizes.triangle(grey_img)
print('triangle threshold:', thr)


