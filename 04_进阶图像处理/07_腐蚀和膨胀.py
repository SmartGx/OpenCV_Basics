# 腐蚀和膨胀
import cv2
import numpy as np

img = cv2.imread('../Datasets/love.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
# 膨胀操作
dilateImg = cv2.dilate(img, kernel)
# 腐蚀操作
erodeImg = cv2.erode(img, kernel)

cv2.imshow('SrcImg', img)
cv2.imshow('dilateImg', dilateImg)
cv2.imshow('erodeImg', erodeImg)

cv2.waitKey(0)
cv2.destroyAllWindows()