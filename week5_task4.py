#4.Fill 2 arrays with some values and calculate the sum array.

from array import *

arr1 = array('i', [1,2,3,4,5,6,7])
arr2 = array('i', [8,9,10,11,12,13,14])

arr3 = arr1 + arr2
print(arr3)
print(sum(arr1))
print(sum(arr2))
print(sum(arr3))