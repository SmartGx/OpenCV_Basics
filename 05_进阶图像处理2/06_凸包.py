# 凸包
import cv2
import numpy as np

img = cv2.imread('../Datasets/dingdangcat.jpg')
# 图像预处理
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresholdImg = cv2.threshold(grayImg, 100, 255, cv2.THRESH_BINARY)

# 获得轮廓
_, contours, hierarchy = cv2.findContours(thresholdImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 外边轮廓
x, y, w, h = cv2.boundingRect(contours[1])
cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
# 计算并绘制凸包
hull = cv2.convexHull(contours[1], True)
cv2.polylines(img, [hull], True, (255, 0, 0), 3)

cv2.imshow("Img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()