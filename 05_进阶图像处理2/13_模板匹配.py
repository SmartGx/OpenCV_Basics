# 模板匹配
"""
使用cv2.matchTemplate()进行模板匹配
method:
	1. 匹配值越高，匹配程度越高的：相关匹配法和归一化相关匹配法（TM_CCORR和TM_CCORR_NORMED），
								系数匹配法和化相关系数匹配法（TM_CCOEFF和TM_CCOEFF_NORMED）
	2. 匹配值越低，匹配程度越高的：平方差匹配法和归一化平方差匹配法（TMSQDIFF和TM_SQDIFF_NORMED）
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('../Datasets/jump1.jpg')
img2 = cv2.imread('../Datasets/jump2.jpg')
temp = cv2.imread('../Datasets/jumpTemp.jpg')

# 灰度化图像
grayImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayTemp = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)

imgGrayCopy = grayImg1.copy()
h, w = grayTemp.shape
# 对模板图像进行阈值化处理
_, grayTempThresh = cv2.threshold(grayTemp, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('temp', grayTempThresh)

# 匹配方法
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED',
			 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
	# 每次都进行一次图片拷贝
	grayImg1 = grayImg1.copy()
	method = eval(meth)
	# 进行模板匹配
	res = cv2.matchTemplate(grayImg1, grayTempThresh, method)
	# 定位匹配坐标
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		top_left = min_loc
	else:
		top_left = max_loc
	# 获得边框的右下角坐标
	bottom_right = (top_left[0] + w, top_left[1] + h)
	# 绘制矩形边框
	cv2.rectangle(grayImg1, top_left, bottom_right, (0, 0, 0), 3)
	plt.subplot(121), plt.imshow(res, cmap='gray')
	plt.title('Match Result'), plt.xticks([]), plt.yticks([])
	plt.subplot(122), plt.imshow(grayImg1, cmap='gray')
	plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
	plt.suptitle(meth)

	plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()