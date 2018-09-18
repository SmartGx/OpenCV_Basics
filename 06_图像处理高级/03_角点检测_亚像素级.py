# 03_角点检测_亚像素
import cv2
import numpy as np

filename = '../Datasets/air.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 使用Harri算法和连通域找到亚像素点
gray32 = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)
ret, dst = cv2.threshold(dst, 0.01*dst.max(), 255, 0)
dst = np.uint8(dst)
cv2.imshow('dst', dst)

# 寻找连通域矩心
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# 确定亚像素角点检测的迭代条件
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(gray32, np.float32(centroids), (5, 5), (-1, -1), criteria)

# 使用Shi-Tomasi算法找到角点
cornerPoints = cv2.goodFeaturesToTrack(gray, 50, 0.01, 50)
cornersS = cv2.cornerSubPix(gray, cornerPoints, (5, 5), (-1, -1), criteria)
# 横向堆叠矩心和角点的坐标矩阵
res = np.hstack((centroids, corners))
res = np.int0(res)
print(res)
# 蓝色点表示Harri算法后找到的角点
# 绿色点表示Harri算法后和连通域找到的亚像素角点
# 红色点表示Shi-Tomasi算法后找到的亚像素角点
for i in cornersS:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 4, [0, 0, 255])
for i in range(0, res[:, 3].size):
    cv2.circle(img, (res[i, 0], res[i, 1]), 4, [255, 0, 0])
    cv2.circle(img, (res[i, 2], res[i, 3]), 3, [0, 255, 0])
cv2.imshow('Image', img)

cv2.waitKey()
cv2.destroyAllWindows()