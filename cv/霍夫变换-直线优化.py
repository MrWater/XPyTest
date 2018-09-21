#-*-coding:utf8-*-

import cv2
import numpy as np

from matplotlib import pyplot as plt


img = cv2.imread("image/5.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

cv2.imshow("gray", edges)
minLineLength = 10
maxLineGap = 10
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)

for i in range(len(lines)):
	for x1, y1, x2, y2 in lines[i]:
		cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()