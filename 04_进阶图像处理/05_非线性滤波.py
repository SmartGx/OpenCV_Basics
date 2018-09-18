# 非线性滤波(中值滤波、双边滤波)
"""
#-----------------------------------中值滤波----------------------------------
import cv2
import numpy as np

def medianBlur(x):
	pass

img = cv2.imread('../Datasets/3.jpg')

cv2.namedWindow('median Blur')
cv2.createTrackbar('ksize', 'median Blur', 1, 30, medianBlur)

while True:
	median_ksize = cv2.getTrackbarPos('ksize', 'median Blur')
	if median_ksize % 2 == 0:
		median_ksize += 1
	# 中值滤波
	medianBlur_img = cv2.medianBlur(img, median_ksize)

	cv2.imshow('median Blur', medianBlur_img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()

"""
#-----------------------------双边滤波-------------------------------
import cv2
import numpy as np

img = cv2.imread('../Datasets/food.jpg')

# 为方便显示 我们将窗口适当缩小
cv2.namedWindow('Bilateral Blur')

BilateralBlurImg = cv2.bilateralFilter(img, 25, 25*2, 25/2)
   
cv2.imshow('Bilateral Blur', BilateralBlurImg)
   
cv2.waitKey()

cv2.destroyAllWindows()