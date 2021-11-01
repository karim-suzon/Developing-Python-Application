#There are 20 values in an array: calculate the standard deviation.

from array import *
import statistics

vals = array('i', [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

print("standard deviation of vals is % s " % (statistics.stdev(vals)))