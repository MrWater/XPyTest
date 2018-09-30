#-*-coding:utf8-*-

import numpy as np

test = [[1],
        [2]]

print(test == eval('test'))

print(eval("(\"test,\" * 4)[:-1]"))
print(np.hstack([test, test, test]))