#mean var and std using numpy

import numpy as np 
#due to formatting issues in the test case. need to default to earlier version
np.set_printoptions(legacy='1.13')

#N and M array dimensions
N,M= map(int,input().split())

#enter array details constrained by the dimensions above
a=np.array([input().split()[:M] for _ in range(N)], dtype=int)

#the std output is truncated to 11 decimal points
print(np.mean(a, axis=1), np.var(a, axis=0), np.round(np.std(a,axis=None),11), sep='\n')