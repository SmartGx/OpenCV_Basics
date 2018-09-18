# 05_SIFT特征匹配
import cv2
import numpy as np

img1 = cv2.imread('../Datasets/Mavic_Air_Fly.jpeg')
img2 = cv2.imread('../Datasets/Mavic_Air_Fly_yuntai.jpeg')
matchImg = np.zeros_like(img1)

grayImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayImg2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 创建sift对象
sift = cv2.xfeatures2d.SIFT_create()
# 检测并计算图1的关键点向量和关键点描述
kp1, dest1 = sift.detectAndCompute(grayImg1, None)
kp2, dest2 = sift.detectAndCompute(grayImg2, None)

"""
# 创建暴力匹配对象
bf = cv2.BFMatcher_create(normType=cv2.NORM_L2, crossCheck=True)
# 进行特征匹配
matches = bf.match(dest1, dest2)
matches = sorted(matches, key=lambda x: x.distance)
# 绘制
matchImg = cv2.drawMatches(img1, kp1, img2, kp2, matches, matchImg, flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
"""

# 使用knn匹配
bf = cv2.BFMatcher_create(normType=cv2.NORM_L2, crossCheck=False)
matches = bf.knnMatch(dest1, dest2, k=2)
# 使用阈值筛选距离
good = []
for m, n in matches:
	if m.distance < 0.05*n.distance:
		good.append([m])

matchImg = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, matchImg, flags=2)

cv2.imshow('Match result', matchImg)
cv2.waitKey(0)
cv2.destroyAllWindows()