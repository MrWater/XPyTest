#-*-coding:utf8-*-

import cv2
import numpy as np

from matplotlib import pyplot as plt


img = cv2.imread("image/4.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 255, 255, apertureSize=3)

cv2.imshow("gray", edges)
lines = cv2.HoughLines(edges, 1, np.pi/180, 178)

for i in range(len(lines)):
	for rho, theta in lines[i]:
		a = np.cos(theta)
		b = np.sin(theta)
		x0 = a * rho
		y0 = b * rho
		x1 = int(x0 + 1000 * -b)
		y1 = int(y0 + 1000 * a)
		x2 = int(x0 - 1000 * -b)
		y2 = int(y0 - 1000 * a)

		print(x1, y1, x2, y2)
		cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()