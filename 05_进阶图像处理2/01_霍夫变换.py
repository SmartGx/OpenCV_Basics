# 霍夫变换
import cv2
import numpy as np


def drawFindLines(img, lines):
	for i in lines:
		for rho, theta in i:
			a = np.cos(theta)
			b = np.sin(theta)
			# 变换到x-y坐标系
			x0 = a * rho
			y0 = b * rho
			# 用点和斜率得到直线上的两个点
			x1 = int(x0 + 1000 * (-b))
			y1 = int(y0 + 1000 * (a))
			x2 = int(x0 - 1000 * (-b))
			y2 = int(y0 - 1000 * (a))
			cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)


img = cv2.imread('../Datasets/rand.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 边缘检测
edges = cv2.Canny(grayImg, 50, 120, apertureSize=3)
cv2.imshow('cannyImg', edges)

# 三维的直线集合.第一维为直线条数，第二维和第三维为对应的rho和theta
lines = cv2.HoughLines(edges, 1, np.pi/180, 250)
drawFindLines(img, lines)
cv2.imshow('Line', img)

cv2.waitKey(0)
cv2.destroyAllWindows()