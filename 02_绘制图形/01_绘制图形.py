# 绘制直线，方框，圆形和文本框
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# 绘制一条绿线
img = cv2.line(img, (0, 0), (100, 100), (0, 255, 0), 2)
# 绘制一个矩形
img = cv2.rectangle(img, (100, 100), (300, 300), (0, 0, 255), 4)
# 绘制一个圆形(-1表示为实心)
img = cv2.circle(img, (200, 200), 100, (0, 255, 255), -1)
# 绘制一个文本框
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (150, 500), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()