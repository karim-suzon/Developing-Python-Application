#5.Returns the biggest of 3 integers.

def big_one(x,y,z):
    if x > y:
        return x
    elif y > z:
        return y
    else:
        return z

result = big_one(7,23,9)
print(result)