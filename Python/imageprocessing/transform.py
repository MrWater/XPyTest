# !/user/bin/python
# -*-coding:utf8-*-

from PIL import Image

import matplotlib.pyplot as ptl

img = Image.open(r'C:\Users\WX\Desktop\test.jpg')
dst = img.rotate(45)
# dst = img.transpose(Image.FLIP_LEFT_RIGHT)
# dst = img.transpose(Image.FLIP_TOP_BOTTOM)
# dst = img.transpose(Image.ROTATE_90)

ptl.figure('transform')
ptl.imshow(dst)
ptl.show()