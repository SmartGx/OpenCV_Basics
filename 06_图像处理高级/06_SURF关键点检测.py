# 06_SURF关键点检测
import cv2
import numpy as np

img = cv2.imread('../Datasets/Mavic_Air_Fly.jpeg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建surf对象
surf = cv2.xfeatures2d.SURF_create(500, upright=True)
# 检测关键点并计算关键点特征
kp, des = surf.detectAndCompute(grayImg, None)
# 绘制关键点
img2 = cv2.drawKeypoints(img, kp, None, (0, 255, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('SURF Image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()