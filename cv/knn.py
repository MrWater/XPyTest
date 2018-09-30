# -*-coding:utf8-*-

import cv2
import numpy as np
import matplotlib.pyplot as plt


trainning_data = np.random.randint(0, 100, (25, 2)).astype(np.float32)
responses = np.random.randint(0, 3, (25, 1)).astype(np.float32)

red = trainning_data[responses.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')

blue = trainning_data[responses.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 's')

green = trainning_data[responses.flatten() == 2]
plt.scatter(green[:, 0], green[:, 1], 80, 'g', '*')

new_comer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(new_comer[:, 0], new_comer[:, 1], 80, 'g', 'o')

knn = cv2.ml.KNearest_create()
knn.train(trainning_data, cv2.ml.ROW_SAMPLE, responses)
ret, results, neighbours, dist = knn.findNearest(new_comer, 3)

print("result: ", results)
print("neighbours: ", neighbours)
print("distance: ", dist)

plt.show()