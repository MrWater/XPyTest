#! /uer/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image

import matplotlib.pyplot as ptl
import numpy

img = Image.open(r'C:\Users\WX\Desktop\test.png').convert('L')
img = numpy.array(img) # get the martix form image

rows,cols = img.shape
for i in range(rows):
	for j in range(cols):
		if img[i,j] <= 128:
			img[i,j] = 0
		else:
			img[i,j] = 1

ptl.figure('pixel')
ptl.axis('off')
ptl.imshow(img, cmap='gray')
ptl.show()