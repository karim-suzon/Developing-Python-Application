#12.Calculates an approximation of Neper's value(e).

def calc_e(n):
    e = (1.0 + 1.0 / n)**n
    return e
print(calc_e(1000))