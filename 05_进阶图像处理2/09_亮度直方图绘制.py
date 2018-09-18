# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 22:26
# @Author  : SmartGx
# @Note    : 
# @File    : 09_直方图绘制.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Datasets/place.jpg')
cv2.imshow('srcImg', img)

fig = plt.figure(figsize=(16, 10))
# 图像灰度化
grayImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ax1 = fig.add_subplot(3, 2, 1)
ax1.set_title('GrayImg')
# Note:使用plt显示灰度图,需要添加cmap='gray'参数
# Note:使用plt.imshow显示彩色图,需要将cv2打开的图片通道由bgr转化为rgb,即img = img[:, :, [2,1,0]]
ax1.imshow(grayImg, cmap='gray')
# 计算灰度图像直方图
grayHist = cv2.calcHist([grayImg], [0], None, [256], [0, 256])
ax2 = fig.add_subplot(3, 2, 2)
ax2.set_title('GrayHist')
ax2.plot(grayHist)

# 计算彩色图像直方图
color = ('b', 'g', 'r')
ax3 = fig.add_subplot(3, 2, 3)
ax3.set_title('BGR Hist')
for i, col in enumerate(color):
	bgrHist = cv2.calcHist([img], [i], None, [256], [0, 256])
	ax3.plot(bgrHist, color=col)
	plt.xlim([0, 256])
	
# 掩膜处理
mask = np.zeros(grayImg.shape[:2], np.uint8)
mask[200:500, 300:600] = 255
masked_img = cv2.bitwise_and(grayImg, grayImg, mask=mask)
ax4 = fig.add_subplot(3, 2, 4)
ax4.set_title('mask')
ax4.imshow(mask, cmap='gray')

ax5 = fig.add_subplot(3, 2, 5)
ax5.set_title('masked_img')
ax5.imshow(masked_img, cmap='gray')

# 计算带掩膜直方图
hist_mask = cv2.calcHist([grayImg], [0], mask, [256], [0, 256])
# 计算不带掩膜直方图
hist_full = cv2.calcHist([grayImg], [0], None, [256], [0, 256])
ax6 = fig.add_subplot(3, 2, 6)
ax6.set_title('mask_hist')
ax6.plot(hist_full, label='hist_full')
ax6.plot(hist_mask, label='hist_mask')
plt.xlim([0, 256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
