# 移动鼠标并按下Ctrl键画圆
import cv2
import numpy as np

# 回调函数（双击鼠标左键画一个蓝色的实心圆）
def draw_circle(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		print(param)
		cv2.circle(img, (x, y), 100, (255, 0, 0), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle, 'draw a blue circle.\n(Enter esc to exit!)')

while True:
	cv2.imshow('image', img)
	if cv2.waitKey(20) & 0xFF == 27:
		break
cv2.destroyAllWindows()
