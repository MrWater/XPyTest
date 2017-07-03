#! /uer/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image

import matplotlib.pyplot as ptl

img = Image.open(r'C:\Users\WX\Desktop\test.jpg')
box = (80, 100, 260, 300)
roi = img.crop(box)

ptl.figure('clip')

ptl.subplot(1, 2, 1)
ptl.title('origin')
ptl.axis('off')
ptl.imshow(img)

ptl.subplot(1, 2, 2)
ptl.title('roi')
ptl.axis('off')
ptl.imshow(roi)

ptl.show()
