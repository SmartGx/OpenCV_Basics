# 07_SURF特征匹配
import cv2
import numpy as np

img1 = cv2.imread('../Datasets/Mavic_Air_Fly.jpeg')
img2 = cv2.imread('../Datasets/Mavic_Air_Fly_yuntai.jpeg')
# 图像灰度化
grayImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayImg2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
matchImg = np.zeros_like(img1)

# 创建SURF对象
surf = cv2.xfeatures2d.SURF_create(2000)
# 检测关键点并且计算关键点描述
kp1, des1 = surf.detectAndCompute(grayImg1, None)
kp2, des2 = surf.detectAndCompute(grayImg2, None)

# 创建暴力匹配对象
bf = cv2.BFMatcher_create(crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x:x.distance)
matchImg = cv2.drawMatches(img1, kp1, img2, kp2, matches, matchImg, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv2.imshow('SURF Image', matchImg)
cv2.waitKey(0)
cv2.destroyAllWindows()