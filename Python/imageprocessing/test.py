#! /uer/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wx'

from PIL import Image # library for showing image

import matplotlib.pyplot as plt # library for processing image


img = Image.open(r'C:\Users\WX\Desktop\test.jpg')

print(vars(img))

plt.figure('python_imageprocess')

gray = img.convert('L') 
# convert: change the color mode
# 1: 1-bit pixels, black and white, stored with one pixel per byte
# L: 8-bit pixels, black and white
# P: 8-bit pixels, mapped to any other mode using a color palette
# RGB: 3*8-bit pixels, true color
# RGBA: 4*8-bit pixels, true color with transparency mask
# ...

r,g,b = img.split()
pic = Image.merge('RGB', (r,g,b))

plt.subplot(2,3,1)
plt.title('origin')
plt.axis('off')
plt.imshow(img)

plt.subplot(2,3,2)
plt.title('gray')
plt.axis('off')
plt.imshow(gray, cmap='gray')

plt.subplot(2,3,3)
plt.title('merge')
plt.axis('off')
plt.imshow(pic)

plt.subplot(2,3,4)
plt.title('r')
plt.axis('off')
plt.imshow(r, cmap='gray')

plt.subplot(2,3,5)
plt.title('g')
plt.axis('off')
plt.imshow(g, cmap='gray')

plt.subplot(2,3,6)
plt.title('b')
plt.axis('off')
plt.imshow(b, cmap='gray')

print(type(r))

plt.show()
