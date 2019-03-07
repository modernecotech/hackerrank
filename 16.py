#numpy linear algebra

import numpy as np


#due to formatting issues in the test case. need to default to earlier version
np.set_printoptions(legacy='1.13')

N=int(input())
A=np.array([input().split() for _ in range(N)], dtype=float)

print(np.linalg.det(A))