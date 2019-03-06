#numpy floor celing rint

import numpy as np 

#add a space in front of each element in array
np.set_printoptions(sign=' ')
#input a space separated one dimensional array of floating points
a=np.array(input().split(),float)
#print out the floor, ceil and rint separated by a newline
print(np.floor(a),np.ceil(a),np.rint(a), sep='\n')
