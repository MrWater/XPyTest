# -*-coding:utf8-*-

import numpy as np
import keras

test_vec = np.array([[1, 2], [2, 3, 4], [1]])
print(test_vec)
print(keras.preprocessing.sequence.pad_sequences(test_vec))