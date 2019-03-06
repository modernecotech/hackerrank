#sum and prod using numpy
import numpy as np
#N and M array dimensions
N,M= map(int,input().split())

#enter array details constrained by the dimensions above
a=np.array([input().split()[:M] for _ in range(N)], dtype=int)

print(np.prod(np.sum(a, axis=0), axis=0))