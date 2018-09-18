# 10_ORB算法特征点检测
import numpy as np
import cv2

img = cv2.imread('../Datasets/Mavic_Air_Fly.jpeg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建一个ORB对象
orb = cv2.ORB_create(nfeatures=200)

kp, des = orb.detectAndCompute(grayImg, None)

img2 = cv2.drawKeypoints(img, kp, None, (0, 255, 0), 0)

cv2.imshow('KP', img2)
cv2.waitKey()
cv2.destroyAllWindows()