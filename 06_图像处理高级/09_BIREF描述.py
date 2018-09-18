# 09_BIREF描述
import numpy as np
import cv2

img = cv2.imread('../Datasets/Mavic_Air_Fly.jpeg')
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建一个CenSurE检测器 这是论文中推荐的检测器
star = cv2.xfeatures2d.StarDetector_create()

# 创建一个brief描述
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

# 检测关键点并生成描述
kp = star.detect(img, None)
kp, des = brief.compute(img, kp)

print(des)

print(des.shape)