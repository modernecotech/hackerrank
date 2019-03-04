#!/bin/python3

N=int(input())

if N%2 is not 0:
    print("Weird")
elif 2<= N <=5 :
    print("Not Weird")
elif 6<= N <= 20:
    print("Weird")
elif 20 > N < 100:
    print("Not Weird")
