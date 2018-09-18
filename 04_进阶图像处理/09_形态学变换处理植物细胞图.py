# 形态学变换处理植物细胞图
import cv2
import numpy as np

cellSrcImg = cv2.imread('../Datasets/cell.jpg')
cv2.imshow('cellSrcImg', cellSrcImg)

# 将图像转化为灰度图
cellGrayImg = cv2.cvtColor(cellSrcImg, cv2.COLOR_BGR2GRAY)
# 阈值化处理
teval, grayThreshImg = cv2.threshold(cellGrayImg, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('cellGrayImg', grayThreshImg)

# 开运算处理
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
cellMorphImg = cv2.morphologyEx(cellGrayImg, cv2.MORPH_OPEN, kernel)
cv2.imshow('cellMorpgImg', cellMorphImg)

cv2.waitKey(0)
cv2.destroyAllWindows()