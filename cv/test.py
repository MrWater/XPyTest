#-*-coding:utf8-*-

import numpy as np

arr = np.random.random((2, 2, 2, 3))
print(arr)
np.random.shuffle(arr)
print(arr)