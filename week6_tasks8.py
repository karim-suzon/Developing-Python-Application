#8.Calculates amount of combinations (try to use also an own factorial function here.)

from itertools import combinations


def combine(arr, s):
    return list(combinations(arr, s))


array = [21, 18, 19]
set = 2
print(combine(array, set))