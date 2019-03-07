#python numpy inner/outer example. returns product of two arrays

import numpy as np 

#due to formatting issues in the test case. need to default to earlier version
np.set_printoptions(legacy='1.13')

a,b=(np.array([input().split()], dtype=int) for _ in range(2))

print(np.inner(a,b)[0][0], np.outer(a,b), sep='\n')

