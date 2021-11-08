#7.Function returns the biggest of 5 integers.


def biggest_one_among5int(a,b,c,d,f):
    if a > b:
        return a
    elif b > c:
        return b
    elif c > d:
        return c
    elif d > f:
        return d
    else:
        return f
result = biggest_one_among5int(3,5,9,2,11)
print(result)