# 霍夫圆变换
import cv2
import numpy as np

img = cv2.imread('../Datasets/opencv_logo.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(grayImg, cv2.HOUGH_GRADIENT, 2, 50)

for i in circles:
	for x,y,r in i:
		cv2.circle(img, (x, y), r, (0, 0, 0), 2)

cv2.imshow('Circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()