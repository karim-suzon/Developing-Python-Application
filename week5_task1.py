# 1. Array contains 30 random values. Calculate the sum and average.
#In array we need to have all the values of same type
#In list we can have like int, tuple and string mixed but in array it has to be same value

#from array import *

#arr = array('i', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])

#av = len(arr)/2


#print(sum(arr))
#print(av)

import random

array = list(range(1,31))
average = len(array)/2

print(sum(array))
print(average)