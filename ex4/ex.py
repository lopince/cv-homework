import binarizes
import imgs
import morphologys


# 读取图片
img = imgs.read('test.jpg')

# 转化为灰度图
grey_img = imgs.to_grey_img(img)

# 二值化

# 大津法—最大类间方差法
thr, ostu_binary_img = binarizes.ostu(grey_img)
print('ostu threshold:', thr)
imgs.write("ostu_binary.jpg", ostu_binary_img)

# triangle
thr, triangle_binary_img = binarizes.triangle(grey_img)
print('triangle threshold:', thr)
imgs.write('triangle_binary.jpg', triangle_binary_img)

# binary
thr, binary_img = binarizes.binary(grey_img)
print('binary threshold:', thr)
imgs.write('binary.jpg', binary_img)

# binary inv
thr, binary_inv_img = binarizes.binary_inv(grey_img)
print('binary inv threshold:', thr)
imgs.write('binary_inv.jpg', binary_inv_img)

# trunc
thr, trunc_binary_img = binarizes.trunc(grey_img)
print('trunc binary threshold:', thr)
imgs.write('trunc_binary.jpg', trunc_binary_img)

# to zero
thr, to_zero_binary_img = binarizes.tozero(grey_img)
print('to zero binary threshold:', thr)
imgs.write('to_zero_binary.jpg', to_zero_binary_img)

# 腐蚀
erosion_img = morphologys.erosion(img)
imgs.write('enosion.jpg', erosion_img)

# 膨胀
dilation_img = morphologys.dilation(img)
imgs.write('dilation.jpg', dilation_img)

# 闭运算
morph_close_img = morphologys.morph_close(img)
imgs.write('morph_close.jpg', morph_close_img)

# 开运算
morph_open_img = morphologys.morph_open(img)
imgs.write('morph_open.jpg', morph_open_img)

# 细化
ostu_binary_thinning_img = morphologys.thinning(ostu_binary_img)
imgs.write('ostu_binary_thinning.jpg', ostu_binary_thinning_img)

triangle_binary_thinning_img = morphologys.thinning(triangle_binary_img)
imgs.write('triangle_binary_thinning.jpg', triangle_binary_thinning_img)

binary_thinning_img = morphologys.thinning(binary_img)
imgs.write('binary_thinning.jpg', binary_thinning_img)

binary_inv_thinning_img = morphologys.thinning(binary_inv_img)
imgs.write('binary_inv_thinning.jpg', binary_inv_thinning_img)

trunc_binary_img = morphologys.thinning(trunc_binary_img)
imgs.write('trunc_binary_thinning.jpg', trunc_binary_img)

to_zero_binary_img = morphologys.thinning(to_zero_binary_img)
imgs.write('to_zero_binary_thinning.jpg', to_zero_binary_img)
