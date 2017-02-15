# !/user/bin/python
# -*-coding:utf8-*-

__author__ = 'x'

import numpy as np
import matplotlib.pyplot as ptl

from PIL import Image # library for processing image

image_path = './imgs/'
num = 100

img = Image.open(image_path + str(np.random.randint(num)) + ".jpg").convert('L')
img_arr = np.array(img)

rows,cols = img_arr.shape
for i in range(rows):
	for j in range(cols):
		if img_arr[i,j] <= 128:
			img_arr[i,j] = 0
		else:
			img_arr[i,j] = 1

ptl.figure('captcha')
ptl.imshow(img_arr, cmap='gray')
ptl.axis('off')
ptl.show()
