# 对图像进行加权相加
import cv2
import numpy as np

img1 = cv2.imread('../Datasets/mogu.jpg')
img2 = cv2.imread('../Datasets/rain.jpg')

# 对两幅图像进行加权相加
img3 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

cv2.namedWindow('img1')
cv2.namedWindow('img2')
cv2.namedWindow('img3')
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.imwrite('rain_mogu.jpg', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()