# 打开摄像头
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
	if cap.isOpened():
		ret, frame = cap.read()
		cv2.imshow('Camera', frame)
		# 延时30ms，如果按下退出键q，则退出
		if cv2.waitKey(30)&0xFF is ord('q'):
			break
cv2.destroyAllWindows()