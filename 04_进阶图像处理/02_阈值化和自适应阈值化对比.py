# 普通阈值化和自适应阈值化效果对比
import cv2
import numpy as np

img = cv2.imread('../Datasets/girl.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 适当调整窗口大小
cv2.namedWindow('Thresh Window', cv2.WINDOW_NORMAL)
cv2.namedWindow('BGR Thresh Window', cv2.WINDOW_NORMAL)
cv2.namedWindow('Adaptive Thresh Window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Thresh Window', (640, 480))
cv2.resizeWindow('BGR Thresh Window', (640, 480))
cv2.resizeWindow('Adaptive Thresh Window', (640, 480))

# 使用灰度图阈值化处理
retval, threshImg = cv2.threshold(img_gray, 122, 255, cv2.THRESH_BINARY)
# 使用彩色图阈值化处理
retval, bgrThreshImg = cv2.threshold(img, 122, 255, cv2.THRESH_BINARY)
# 使用灰度自适应阈值化处理
adaptiveThreshImg = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 49, 0)


# 显示图片
cv2.imshow('Thresh Window', threshImg)
cv2.imshow('BGR Thresh Window', bgrThreshImg)
cv2.imshow('Adaptive Thresh Window', adaptiveThreshImg)

cv2.waitKey(0)
cv2.destroyAllWindows()