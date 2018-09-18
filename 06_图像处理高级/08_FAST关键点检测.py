# 08_FAST关键点检测
import numpy as np
import cv2

img = cv2.imread('../Datasets/Mavic_Air_Fly.jpeg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建fast对象
fast = cv2.FastFeatureDetector_create(threshold=35)
# 关键点检测
kp = fast.detect(grayImg, None)
img2 = cv2.drawKeypoints(img, kp, None, (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

print('Threshold: ', fast.getThreshold())
print('nonmaxSuppression: ', fast.getNonmaxSuppression())
print('neighborhood: ', fast.getType())
print('Total Keypoints with nonmaxSuppression: ', len(kp))
cv2.imshow('fast_true', img2)

# 不设置非极大值抑制
fast.setNonmaxSuppression(False)
kp = fast.detect(grayImg, None)
print('Total Keypoints without nonmaxSuppression: ', len(kp))

img3 = cv2.drawKeypoints(img, kp, None, (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('fast_false', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()