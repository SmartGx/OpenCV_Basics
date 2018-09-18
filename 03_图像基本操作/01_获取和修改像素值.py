# 获取和修改像素值

     	
# ----------------------1. 直接从矩阵获取像素值----------------
import cv2
import numpy as np

img = cv2.imread('../Datasets/cat.jpg')
img_copy = img.copy()
# 直接获取并修改

pix_bgr = img_copy[100, 100]         # 获取的是三通道的像素值
print(pix_bgr)

pix_bgr_g = img_copy[100, 100, 1]    # 获取的是g通道像素值
print(pix_bgr_g)

img_copy[100, 100] = [0, 0, 1]		 # 直接修改像素值
print(img_copy[100, 100])


# ---------------2. 通过numpy的函数从矩阵中间接获取----------------

pix = img_copy.item(100, 100, 2)		# 使用numpy的item方法获取像素值
print(pix)

img.itemset((100, 100, 1), 255)			# 使用numpy的itemset方法修改像素