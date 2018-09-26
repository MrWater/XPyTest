#-*-coding:utf8-*-

import cv2
import numpy as np 
import time

from matplotlib import pyplot as plt


vc = cv2.VideoCapture("video/1.mp4")
cnt = 0

template = cv2.imread("image/douyin.jpg", 0)
_, template = cv2.threshold(template, 250, 255, cv2.THRESH_BINARY_INV)
w, h = template.shape[::-1]

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

while vc.isOpened():
	ret, frame = vc.read()
	frame_w, frame_h, _ = frame.shape

	if not ret:
		break
	# cnt += 1

	# if cnt >= 2:
	# 	break

	img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	_, thresh = cv2.threshold(img, 245, 255, cv2.THRESH_BINARY)
	thresh = cv2.dilate(thresh, kernel, iterations=4)
	#thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=10)

	img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	img = frame.copy()
	for i in range(len(contours)):
		cnt = contours[i]

		area = cv2.contourArea(cnt)
		hull = cv2.convexHull(cnt)
		hull_area = cv2.contourArea(hull)

		if area < 3000:
			continue

		(x,y), (MA,ma), angle = cv2.fitEllipse(cnt)
		max_angle = (np.pi * 10 / 180)
		#print(area/hull_area)
		if angle > max_angle and angle < (np.pi/2 - max_angle) or (area/hull_area < 0.8):
			continue

		epsilon = 0.01 * cv2.arcLength(cnt, True)
		approx = cv2.approxPolyDP(cnt,epsilon,True)
		black_img = np.zeros((frame_w, frame_h), np.uint8)
		mask_img = cv2.drawContours(black_img, [cnt], -1, (255, 255, 255), -1)
		#img = cv2.drawContours(img, [cnt], -1, (255, 255, 255), -1)

		#img1 = cv2.inpaint(img, mask_img, 3, cv2.INPAINT_TELEA)
		img = cv2.inpaint(img, mask_img, 3, cv2.INPAINT_NS)
	# img = cv2.drawContours(frame, contours, -1, (0, 255, 0), 1)

	cv2.imshow("img1", frame)
	cv2.imshow("img2", img)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		break

vc.release()
cv2.destroyAllWindows()