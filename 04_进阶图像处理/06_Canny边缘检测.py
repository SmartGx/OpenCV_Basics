# Canny边缘检测
import cv2
import numpy as np

img = cv2.imread('../Datasets/hand.jpg')
# 使用高斯滤波器，消除干扰
blur_img = cv2.GaussianBlur(img, (9, 9), 0)
# 使用Canny进行边缘检测
canny_img = cv2.Canny(blur_img, 50, 130)

cv2.namedWindow('Canny')
cv2.namedWindow('Blur')
cv2.imshow('Canny', canny_img)
cv2.imshow('Blur', blur_img)

cv2.waitKey(0)
cv2.destroyAllWindows()