# 04_SIFT算法
import cv2
import numpy as np
img = cv2.imread('../Datasets/air.jpg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建一个SIFT对象
sift = cv2.xfeatures2d.SIFT_create()
# sift检测关键点
kp = sift.detect(grayImg, None)
# 计算关键点描述
_, des = sift.compute(grayImg, kp)

# 绘制关键点
cv2.drawKeypoints(img, kp, img)
cv2.imshow('Key Points', img)

cv2.waitKey(0)
cv2.destroyAllWindows()