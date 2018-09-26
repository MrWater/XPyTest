#-*-coding:utf8-*-

import cv2
import numpy as np


img = cv2.imread("image/coin.png", 0)
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=3)

sure_bg = cv2.dilate(opening, kernel, iterations=3)
dist_transform = cv2.distanceTransform(opening, 1, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)

sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

ret, markers1 = cv2.connectedComponents(sure_fg)
markers = markers1+1
markers[unknown == 255] = 0

print(markers)

markers3 = cv2.watershed(img, markers)
img[markers3 == -1] = [255, 0, 0]

cv2.imshow("coin", img)
cv2.waitKey()
cv2.destroyAllWindows()
