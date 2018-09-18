import cv2
import numpy as np

class Segmenter(object):
   def __init__(self):
      self._mask_32S = None
      self._waterImg = None
# 将掩膜转化为CV_32S
   def setMark(self, mask):
      self._mask_32S = np.int32(mask)
# 进行分水岭操作
   def waterProcess(self, img):
      self._waterImg = cv2.watershed(img, self._mask_32S)
# 获取分割后的8位图像
   def getSegmentationImg(self):
      segmentationImg = np.uint8(self._waterImg)
      return segmentationImg
# 处理分割后图像的边界值
   def getWaterSegmentationImg(self):
      waterSegmentationImg = np.copy(self._waterImg)
      waterSegmentationImg[self._waterImg == -1] = 1
      waterSegmentationImg = np.uint8(waterSegmentationImg)
      return waterSegmentationImg
# 将分水岭算法得到的图像与源图像合并 实现抠图效果
   def mergeSegmentationImg(self, waterSegmentationImg, isWhite = False):
      _, segmentMask = cv2.threshold(waterSegmentationImg, 250, 1, cv2.THRESH_BINARY)
      segmentMask = cv2.cvtColor(segmentMask, cv2.COLOR_GRAY2BGR)
      mergeImg = cv2.multiply(img, segmentMask)
      if isWhite is True:
         mergeImg[mergeImg == 0] = 255
      return mergeImg

def getBoundingRect(img, pattern):
   _, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   x, y, w, h = cv2.boundingRect(contours[1])
   cv2.rectangle(pattern, (x, y), (x + w, y + h), (0, 0, 200), 2)

img = cv2.imread('../Datasets/UAV.jpg')
mySegmenter = Segmenter()
# 获取前景图片
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurImg = cv2.blur(grayImg, (3, 3))
_, binImg = cv2.threshold(blurImg, 30, 255, cv2.THRESH_BINARY_INV)
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
fgImg = cv2.morphologyEx(binImg, cv2.MORPH_CLOSE, kernel1)
# 获取背景图片
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dilateImg = cv2.dilate(binImg, kernel2, iterations=4)
_, bgImg = cv2.threshold(dilateImg, 1, 128, cv2.THRESH_BINARY_INV)
# 合成掩膜
maskImg = cv2.add(fgImg, bgImg)
mySegmenter.setMark(maskImg)
# 进行分水岭操作 并获得分割图像
mySegmenter.waterProcess(img)
waterSegmentationImg = mySegmenter.getWaterSegmentationImg()
outputImgWhite = mySegmenter.mergeSegmentationImg(waterSegmentationImg,True)
kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))
dilateImg = cv2.dilate(waterSegmentationImg, kernel3)
_, dilateImg = cv2.threshold(dilateImg, 130, 255, cv2.THRESH_BINARY)
# 寻找轮廓
getBoundingRect(dilateImg, img)
cv2.imshow('Contours Image', dilateImg)
cv2.imshow('White Image', outputImgWhite)
cv2.imshow('Mask Image', maskImg)
cv2.imshow('Output Image', img)
cv2.waitKey()
cv2.destroyAllWindows()
