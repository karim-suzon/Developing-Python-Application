#Program calculates the factorial of n(given in a variable)

# Factorial 5! = 5*4*3*2*1/1*2*3*4*5 = 120




def fact(n):
    if n==0:                     # factorial 0! = 1
        return 1
    return n * fact(n-1)
result = fact(5)
print(result)
