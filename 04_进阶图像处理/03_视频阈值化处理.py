# 视频阈值化处理
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

i = 0
cv2.namedWindow('Camera')
cv2.namedWindow('Thresh img')
while(cap.isOpened()):
	i += 1
	retval, frame = cap.read()
	img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# 阈值化处理
	ret, thresh_img = cv2.threshold(img_gray, 122, 255, cv2.THRESH_BINARY)
	# 显示原始摄像头视频
	cv2.imshow('Camera', frame)

	# 显示阈值化后的视频
	if i % 3 == 0:
		cv2.imshow('Thresh img', thresh_img)
	if cv2.waitKey(25) & 0xff == ord('q'):
		break
cv2.destroyAllWindows()