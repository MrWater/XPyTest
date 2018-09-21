#-*-coding:utf8-*-

import cv2
import numpy as np


img = cv2.imread("image/coin.png", 0)
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
img = cv2.erode(thresh, kernel, iterations=5)

cv2.imshow("coin", img)
cv2.waitKey()
cv2.destroyAllWindows()