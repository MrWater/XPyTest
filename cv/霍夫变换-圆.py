#-*-coding:utf8-*-

import cv2
import numpy as np

from matplotlib import pyplot as plt


img = cv2.imread("image/2.jpg")
himg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(img)
_, thresh1 = cv2.threshold(himg[:,:,0], 156, 255, cv2.THRESH_BINARY)
_, thresh2 = cv2.threshold(himg[:,:,0], 40, 255, 1)
thresh1 |= thresh2
#img = cv2.cvtColor(thresh1, cv2.COLOR_HSV2BGR)
# _, img = cv2.threshold(thresh, 255, 255, cv2.COLOR_HSV2BGR)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.merge([thresh1, thresh1, thresh1])
img = thresh&img
cv2.imshow("image", img)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.Canny(img, 105, 255, apertureSize=5)
# #img = cv2.medianBlur(img, 3)
# # cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
#cv2.imshow("image", img)
# circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 30, param1=50,
# 	param2=50, minRadius=120, maxRadius=180)
# circles = np.uint16(np.around(circles))

# for i in circles[0, :]:
# 	cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
# 	cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

# cv2.imshow("image", cimg)
cv2.waitKey()
cv2.destroyAllWindows()