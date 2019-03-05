#array with numpy

import numpy as np 

#n is rows and m is columns
n,m= map(int,input().split())
#filling the multi dimensional numpy arrays as [per the dimensions laid out above].
#the second range 2 is because there are two arrays, if one wanted to make it 
#an unlimited number of arrays then a third variable would be added to the top (n,m,p)
#and the array numbering also changed to give it a multi-array arrangement and range 
#of arrays changed from 2 to p 
a,b=(np.array([input().split()[:m] for _ in range(n)], dtype=int) for _ in range(2))

print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')
