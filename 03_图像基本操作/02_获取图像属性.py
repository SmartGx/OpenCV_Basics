# 获取图像基本属性
import cv2

img = cv2.imread('../Datasets/cat.jpg')

# 获取图像的长宽和通道数
print('图像的形状为： ', img.shape)
# 获取像素总数（w*h*c）
print('图像的像素总数为： ', img.size)
# 获取像素的数据类型
print('像素值类型为： ', img.dtype)

# 设置ROI区域
ROI = img[200:300, 300:400]
