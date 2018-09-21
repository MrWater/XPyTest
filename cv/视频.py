#-*-coding:utf8-*-

import cv2
import numpy as np 
import time

from matplotlib import pyplot as plt


vc = cv2.VideoCapture("video/1.mp4")
cnt = 0

template = cv2.imread("image/douyin.jpg", 0)
_, template = cv2.threshold(template, 180, 255, cv2.THRESH_BINARY_INV)
w, h = template.shape[::-1]

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

while vc.isOpened():
	ret, frame = vc.read()

	if not ret:
		break
	# cnt += 1

	# if cnt >= 2:
	# 	break

	img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	_, thresh = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
	thresh = cv2.dilate(thresh, kernel, iterations=3)

	img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	img = frame.copy()
	for i in range(len(contours)):
		cnt = contours[i]

		# epsilon = 0.01 * cv2.arcLength(cnt, True)
		# approx = cv2.approxPolyDP(cnt,epsilon,True)
		img = cv2.drawContours(img, [cnt], -1, (0, 255, 0), 2)
	# img = cv2.drawContours(frame, contours, -1, (0, 255, 0), 1)

	cv2.imshow("img", img)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		break

vc.release()
cv2.destroyAllWindows()