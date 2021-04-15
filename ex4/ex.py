import cv2

# 读取图片
img = cv2.imread('test.jpg')

# 转化为灰度图
grey_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# 二值化

# 大津法—最大类间方差法
ostu_type = cv2.THRESH_BINARY | cv2.THRESH_OTSU
otsu_thres, otsu_binary_img = cv2.threshold(grey_img, 0, 255, ostu_type)
print("otsu threshold:", otsu_thres)
cv2.imwrite('otsu_binary_img.jpg', otsu_binary_img)

tri_type = cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE
tri_thres, tri_binary_img = cv2.threshold(grey_img, 0, 255, tri_type)
print("tri threshold:", tri_thres)
cv2.imwrite('tri_binary_img.jpg', tri_binary_img)
