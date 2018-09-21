#-*-coding:utf8-*-

import cv2
import numpy as np

from matplotlib import pyplot as plt


roi = cv2.imread("image/douyin.jpg", 0)
print(roi.shape[::-1])

lst = [1,2,3]
print(lst[::-1])