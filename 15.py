#python numpy poly example

import numpy as np 

#put the P in a list of floating point numbers not an array
P=list(map(float,input().split()))
#x is a single floating point number
x=float(input())
print(np.polyval(P,x))