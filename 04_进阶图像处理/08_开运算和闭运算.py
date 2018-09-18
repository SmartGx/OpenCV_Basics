# 开运算和闭运算
'''
1.开运算：
	先腐蚀后膨胀，用来消除小物体、在纤细点处分离物体、平滑较大物体的边界的同时并不明显改变其面积。
2. 闭运算：
	先膨胀后腐蚀，闭运算能够排除小的黑色区域。
3. 形态学梯度：
	膨胀图与腐蚀图之差，通常用来保留边缘轮廓（不是轮廓和边缘识别）。
'''
import cv2
import numpy as np

img = cv2.imread('../Datasets/food.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
openImg = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closeImg = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradImg = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('openImg', openImg)
cv2.imshow('closeImg', closeImg)
cv2.imshow('gradImg', gradImg)

cv2.waitKey(0)
cv2.destroyAllWindows()