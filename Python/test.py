import numpy as np 

a = np.arange(24)
b = a.reshape(2, 3, 4)
print(b)
print(b.ravel())
