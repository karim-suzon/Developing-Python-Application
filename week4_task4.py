#Program throws dice 100 times and tells amounts of differnt values(1,2,3,4,5 and 6).
#Hints: from random import randint
#scaling example [0, 10]
#value = randint(0, 10)

import random
from collections import defaultdict
dice = defaultdict(int)
for x in range(100):
    dice[random.randint(0, 10)] += 1
print(dice)