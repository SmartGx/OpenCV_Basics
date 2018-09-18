# 11_ORB算法特征匹配
import numpy as np
import cv2

img1 = cv2.imread('../Datasets/Mavic_Air_Fly.jpeg')
img2 = cv2.imread('../Datasets/Mavic_Air_Fly_yuntai.jpeg')
grayImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayImg2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
matchImg = np.zeros_like(img1)

orb = cv2.ORB_create(nfeatures=50)

kp1, des1 = orb.detectAndCompute(grayImg1, None)
kp2, des2 = orb.detectAndCompute(grayImg2, None)

# 创建BF匹配对象 使用Hamming距离
bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)
matchImg = cv2.drawMatches(img1, kp1, img2, kp2, matches, matchImg, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv2.imshow('match', matchImg)
cv2.waitKey()
cv2.destroyAllWindows()