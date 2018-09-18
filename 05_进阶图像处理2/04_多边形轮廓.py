# 多边形轮廓
import cv2
import numpy as np

img = cv2.imread('../Datasets/dingdangcat.jpg')

# 图像预处理
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binImg = cv2.threshold(grayImg, 100, 255, cv2.THRESH_BINARY)
# 寻找轮廓
_, contours, hierarchy = cv2.findContours(binImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 绘制轮廓
cv2.drawContours(img, contours, 1, (0, 255, 0), 2)

# 使用矩形框包围轮廓
x,y,w,h = cv2.boundingRect(contours[1])
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
cv2.imshow('Img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
