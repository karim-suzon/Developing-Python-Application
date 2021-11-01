#5.Generate a lottorow (try to use an array here).

from random import *

lottonumbers = list(range(1,50))

numbers = []

for i in range(5):
    shuffle(lottonumbers)
    x = lottonumbers.pop()
    numbers.append(x)

numbers.sort()
print("The lottonumbers are : ", numbers)

