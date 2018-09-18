# 反向投影
import cv2
import numpy as np
import matplotlib.pyplot as plt

def nothing(x):
	pass

img = cv2.imread('../Datasets/hand1.jpg')
ROI = cv2.imread('../Datasets/ROI.jpg')

# 将图像抓转化为HSV空间
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
roiHSV = cv2.cvtColor(ROI, cv2.COLOR_BGR2HSV)

# 创建H值的滑动条
cv2.namedWindow('BackPro Image')
cv2.createTrackbar('H-Value', 'BackPro Image', 0, 180, nothing)

while True:
	hSize = cv2.getTrackbarPos('H-Value', 'BackPro Image')
	hSize = max(2, hSize)
	# 计算roi区域H-S直方图
	roiHsvHist = cv2.calcHist([roiHSV], [0, 1], None, [hSize, 256], [0, 180, 0, 256])
	cv2.normalize(roiHsvHist, roiHsvHist, 0, 255, cv2.NORM_MINMAX)
	# 根据ROI区域的直方图方向投影
	BackProImg = cv2.calcBackProject([imgHSV], [0, 1], roiHsvHist, [0, 180, 0, 256], 1)
	cv2.imshow('BackPro Image', BackProImg)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()