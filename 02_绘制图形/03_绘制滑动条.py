# 绘制滑动条（RGB调色板)
import cv2
import numpy as np

def nothing(x):
	pass

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# 创建并激活滑动条
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

# 使用一个滑动条作为二值开关
switch = '0: OFF\n1: ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
	cv2.imshow('image', img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	# 获取滑动条的位置
	r = cv2.getTrackbarPos('R', 'image')
	g = cv2.getTrackbarPos('G', 'image')
	b = cv2.getTrackbarPos('B', 'image')
	s = cv2.getTrackbarPos(switch, 'image')
	#混合BGR通道
	if s == 0:
		img[:] = 0
	else:
		img[:] = [b, g, r]

cv2.destroyAllWindows()