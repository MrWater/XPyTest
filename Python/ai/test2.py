# !/user/bin/python
# -*-coding:utf8-*-

__author__ = 'wx'

import numpy as np 
import matplotlib.pyplot as plt

from PIL import Image

plt.figure('lean')

plt.subplot(2,1,1)
arr = np.array(Image.open('./0.jpg')).flatten()
n,bins,patches = plt.hist(arr, bins=256, normed=1, facecolor='green', alpha=0.75)

plt.subplot(2,1,2)
img = Image.open('./imgs/0.jpg')
r,g,b = img.split()
arr = np.array(r).flatten()
plt.hist(arr, bins=256, normed=1, facecolor='r', edgecolor='r', hold=1)
arr = np.array(g).flatten()
plt.hist(arr, bins=256, normed=1, facecolor='g', edgecolor='g', hold=1)
arr = np.array(b).flatten()
plt.hist(arr, bins=256, normed=1, facecolor='b', edgecolor='b')

plt.show()

