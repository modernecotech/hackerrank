#min and max using numpy

import numpy as np 

#N and M array dimensions
N,M= map(int,input().split())

#enter array details constrained by the dimensions above
a=np.array([input().split()[:M] for _ in range(N)], dtype=int)

print(np.max(np.min(a, axis=1), axis=0))