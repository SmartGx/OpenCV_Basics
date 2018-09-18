# 02_角点检测_Tomasi
import cv2
import numpy as np

img = cv2.imread('../Datasets/air.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 输出最多50个角点,角点间最小距离为50
cornerPoints = cv2.goodFeaturesToTrack(grayImg, 50, 0.01, 50)
cornerPoints = np.int0(cornerPoints)

for i in cornerPoints:
	x, y = i.ravel()
	# 绘制角点
	cv2.circle(img, (x, y), 3, [0, 255, 0], -1)
cv2.imshow('Shi-Tomasi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()