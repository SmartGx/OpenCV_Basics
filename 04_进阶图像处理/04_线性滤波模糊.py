# 对图像进行线性滤波（方框滤波，均值滤波和高斯滤波）
import cv2
import numpy as np

def blurTrack(x):
	pass

def gaussianTrack(x):
	pass


img = cv2.imread('../Datasets/food.jpg')

cv2.namedWindow('Blur')
# cv2.resizeWindow('Blur', 480, 640)
cv2.namedWindow('Gaussian Blur')
# cv2.resizeWindow('Gaussian Blur', 480, 640)

cv2.createTrackbar('ksize', 'Blur', 1, 30, blurTrack)
cv2.createTrackbar('ksize', 'Gaussian Blur', 1, 30, gaussianTrack)

while True:
	blurVal = cv2.getTrackbarPos('ksize', 'Blur')
	gaussVal = cv2.getTrackbarPos('ksize', 'Gaussian Blur')

	if gaussVal % 2 == 0:
		gaussVal += 1
	blur_img = cv2.blur(img, (blurVal, blurVal))
	gauss_img = cv2.GaussianBlur(img, (gaussVal, gaussVal),0, None, 0)

	cv2.imshow('Blur', blur_img)
	cv2.imshow('Gaussian Blur', gauss_img)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()