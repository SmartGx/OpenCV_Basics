# 使用Camera进行录像
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# 定义视频的编码格式，Win下支持DIVX编码
fourecc = cv2.VideoWriter_fourcc(*'DIVX')
# 创建VideoWriter对象,第二个参数为编码格式，第三个为FPS，第四个为画面大小
out = cv2.VideoWriter('output.avi', fourecc, 20.0, (640, 480))
while(cap.isOpened()):
	ret, frame = cap.read()
	if ret==True:
		out.write(frame)
		cv2.imshow('Video', frame)
		if cv2.waitKey(1)&0xFF == ord('q'):
			break
	else:
		break
cap.release()
out.release()
cv2.destroyAllWindows()