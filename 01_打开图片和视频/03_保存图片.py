# 实现每间隔5秒，保存一张摄像机截图
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
index = 0
while True:
	index += 1
	ret, frame = cap.read()
	cv2.imshow('Camera', frame)
	if index % 100 == 0:
		img_index = index // 100
		img_name = str(img_index) + '.jpg'
		cv2.imwrite(img_name, frame)
		print(img_name + ' saved.')
	# FPS设置为20
	if cv2.waitKey(50)&0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
