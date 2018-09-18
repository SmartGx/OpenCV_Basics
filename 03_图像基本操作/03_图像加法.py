# 图像相加
import cv2
import numpy as np

# 创建两个图像矩阵
a = np.zeros((500, 500), np.uint8)
b = np.ones((500, 500), np.uint8)

#-------------------------------普通加法, cv2.add()---------------------
# numpy矩阵直接相加
c = a + b
# 使用opencv提供的add方法
d = cv2.add(a, b)

# 显示图像b
cv2.namedWindow('b')
cv2.imshow('b', b)

b = b+120
# 显示b+120
cv2.namedWindow('b+120')
cv2.imshow('b+120', b)

# 显示d
cv2.namedWindow('add')
cv2.imshow('add', d)

# 验证两种相加的方法得到的结果是否相同
print(c.all() == d.all())

cv2.waitKey(0)
cv2.destroyAllWindows()

