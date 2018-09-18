# 直方图对比
'''
使用cv2.compareHist(H1, H2, method)
method:
	1. HISTCMP_CORREL（相关）：函数返回值越大相似度越高,H1_mean和H2_mean是两个直方图的均值
	2. HISTCMP_CHISQR（卡方）：函数返回值越低相似度越高
	3. HISTCMP_INTERSECT（直方图相交）：函数返回值越高相似度越高
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img0 = cv2.imread('../Datasets/screen0.jpg')
img1 = cv2.imread('../Datasets/screen1.jpg')
img2 = cv2.imread('../Datasets/screen2.jpg')

# 转化为灰度图像
grayImg0 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
grayImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
grayImg2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 转化为rgb图像
rbgImg0 = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB)
rbgImg1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
rbgImg2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# 计算灰度直方图
grayImg0Hist = cv2.calcHist([grayImg0], [0], None, [256], [0, 256])
grayImg1Hist = cv2.calcHist([grayImg1], [0], None, [256], [0, 256])
grayImg2Hist = cv2.calcHist([grayImg2], [0], None, [256], [0, 256])

# 直方图对比
result0 = cv2.compareHist(grayImg0Hist, grayImg1Hist, cv2.HISTCMP_CORREL)
result1 = cv2.compareHist(grayImg0Hist, grayImg2Hist, cv2.HISTCMP_CORREL)
result2 = cv2.compareHist(grayImg1Hist, grayImg2Hist, cv2.HISTCMP_CORREL)
# 输出相似比较结果
print('img0与img1相似度为:{:.6f}\n'.format(result0))
print('img0与img2相似度为:{:.6f}\n'.format(result1))
print('img1与img2相似度为:{:.6f}'.format(result2))


# 绘制图像
fig = plt.figure(figsize=(16, 12))
ax1 = fig.add_subplot(2, 3, 1)
ax1.set_title("Img0")
ax1.imshow(rbgImg0)

ax2 = fig.add_subplot(2, 3, 2)
ax2.set_title("Img1")
ax2.imshow(rbgImg1)

ax3 = fig.add_subplot(2, 3, 3)
ax3.set_title("Img2")
ax3.imshow(rbgImg2)

ax4 = fig.add_subplot(2, 3, 4)
ax4.set_title("Img0Hist")
ax4.plot(grayImg0Hist)

ax5 = fig.add_subplot(2, 3, 5)
ax5.set_title("Img1Hist")
ax5.plot(grayImg1Hist)

ax6 = fig.add_subplot(2, 3, 6)
ax6.set_title("Img2Hist")
ax6.plot(grayImg2Hist)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()