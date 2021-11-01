#3.Search a value from an array.

from array import *

arr = array('i', [2,3,4,5,6,7,8,9,10,11,12])

search_val = 8
k = 0
for e in arr:
    if e == search_val:
        print("index number is : ",k)
    k+=1