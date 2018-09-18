'''
OpenCV中进行阈值化处理分为4步：
	1. 载入图像
	2. 转换到灰度空间
	3. 阈值化处理
	4. 显示处理后的图像
'''
import cv2
import numpy as np


# 定义滑动条的回调函数
def threshbar(x):
	pass

img = cv2.imread('../Datasets/girl.jpg')
# 将图像进行灰度化
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Thresh Window')

# 创建阈值滑动条
cv2.createTrackbar('Thresh', 'Thresh Window', 0, 200, threshbar)

while True:
	# 获得滑动条的阈值
	threshVal = cv2.getTrackbarPos('Thresh', 'Thresh Window')
	# 调用阈值化函数进行图像二值化
	retval, threshImg = cv2.threshold(img_gray, threshVal, 255, cv2.THRESH_BINARY)
	cv2.imshow('Thresh Window', threshImg)
	if cv2.waitKey(1) & 0xFF is ord('q'):
		break
cv2.destroyAllWindows()