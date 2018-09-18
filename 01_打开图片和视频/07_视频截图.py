# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 20:23
# @Author  : SmartGx
# @Site    : 
# @File    : capture_imgs.py

import cv2
import os

# 视频存放路径
VIDEO_PATH = 'E://BaiduNetdiskDownload//dpdownload//S01E09.mkv'
# 存放视频帧的路径
IMG_DIR = 'images'
# 帧提取频率
EXTRACT_FREQUENCY = 72


def extract_frames(video_path, img_dir, index):
	"""
	函数功能： 从视频中提取帧
	:param video_path: 视频存放路径
	:param dst_folder: 帧图像存放路径
	:param index: 图片的索引值
	:return: None
	"""
	video = cv2.VideoCapture()
	if not video.open(video_path):
		print("can not open the video")
		exit(1)
	count = 1
	while True:
		_, frame = video.read()
		if frame is None:
			break
		if count % EXTRACT_FREQUENCY == 0:
			save_path = "{}/{:>03d}.jpg".format(img_dir, index)
			cv2.imwrite(save_path, frame)
			print("Extracting %d.jpg" % index)
			index += 1
		count += 1
	video.release()
	print("Totally save {:d} pictures".format(index-1))


def main():
	# 不存在目录则创建
	if not os.path.exists(IMG_DIR):
		os.mkdir(IMG_DIR)
	# 抽取帧图片，并保存到指定路径
	extract_frames(VIDEO_PATH, IMG_DIR, 1)


if __name__ == '__main__':
	main()