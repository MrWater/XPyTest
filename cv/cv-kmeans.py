# -*-coding:utf8-*-

import cv2
import numpy as np
from matplotlib import pyplot as plt


X = np.random.randint(25, 50, (25, 2))
Y = np.random.randint(60, 85, (25, 2))
z = np.vstack((X, Y))
z = np.float32(z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS

compactness, labels, centers = cv2.kmeans(z, 2, None, criteria, 10, flags)

A = z[labels.flatten() == 0]
B = z[labels.flatten() == 1]

plt.scatter(A[:, 0], A[:, 1])
plt.scatter(B[:, 0], B[:, 1], c='r')
plt.scatter(centers[:, 0], centers[:, 1], s=80, c='y', marker='s')
plt.xlabel('Height'), plt.ylabel('Weight')
plt.show()
