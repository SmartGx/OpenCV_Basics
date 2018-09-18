# 轮廓检测
import cv2
import numpy as np

def drawMinAreaRect(img, rect):
	# 转化为矩形四个角点坐标
	box = cv2.boxPoints(rect)
	x0, y0 = box[0]
	for i in range(3):
		x, y = box[i]
		x1, y1 = box[i+1]
		cv2.line(img, (x, y), (x1, y1), (0, 0, 255), 2)
		if i == 2:
			cv2.line(img, (x1, y1), (x0, y0), (0, 0, 255), 2)


img = cv2.imread('../Datasets/dingdangcat.jpg')

# 图像预处理
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binImg = cv2.threshold(grayImg, 100, 255, cv2.THRESH_BINARY)
# 寻找轮廓
_, contours, hierarchy = cv2.findContours(binImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 绘制轮廓
cv2.drawContours(img, contours, 1, (0, 255, 0), 2)
rect = cv2.minAreaRect(contours[1])
drawMinAreaRect(img, rect)

cv2.imshow('Img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
