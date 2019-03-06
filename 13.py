#dot function in numpy

import numpy as np

#array square dimensions
n= int(input())
#
a,b=(np.array([input().split()[:n] for _ in range(n)], dtype=int) for _ in range(2))

print(np.dot(a,b))