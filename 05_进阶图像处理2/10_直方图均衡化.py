# 直方图均衡化
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../Datasets/place.jpg')
b,g,r = cv2.split(img)

# 将图像转化为RGB图像
imgRGB = cv2.merge((r, g, b))
# 对每个颜色通道进行直方图均衡化
equalHistImgBlue = cv2.equalizeHist(b)
equalHistImgGreen = cv2.equalizeHist(g)
equalHistImgRed = cv2.equalizeHist(r)

equalHistImg = cv2.merge((equalHistImgBlue, equalHistImgGreen, equalHistImgRed))
equalHistRgbImg = cv2.merge((equalHistImgRed, equalHistImgGreen, equalHistImgBlue))
fig = plt.figure(figsize=(12, 8))
# 显示原始图像
ax1 = fig.add_subplot(2, 2, 1)
ax1.set_title('Srcimg')
ax1.imshow(imgRGB)

# 显示直方图均衡化之后的图像
ax2 = fig.add_subplot(2, 2, 2)
ax2.set_title('equalHistImg')
ax2.imshow(equalHistRgbImg)

color = ['b', 'g', 'r']
ax3 = fig.add_subplot(2, 2, 3)
ax3.set_title('SrcimgHist')
ax4 = fig.add_subplot(2, 2, 4)
ax4.set_title('equalHist')
for i, col in enumerate(color):
	srcHist = cv2.calcHist([img], [i], None, [256], [0, 256])
	equalHist = cv2.calcHist([equalHistImg], [i], None, [256], [0, 256])
	ax3.plot(srcHist)
	ax4.plot(equalHist)

plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()