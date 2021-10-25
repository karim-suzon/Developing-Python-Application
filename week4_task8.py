#Program calculates the factorial of n(given in a variable)

# Factorial 5! = 5*4*3*2*1/1*2*3*4*5 = 120

def fact(n):                      # defined function
    f = 1                         # variable f = 1
    for i in range(1,n+1):
        f = f*i                   # if value of i and f = 1  f = 1*1 = 1, i = 2, f=1*2=2, i=3, f=2*3=6, i=4, f=6*4=24, i=5, f = 24*5= 120
    return f


x = 5                           # assigned value

result = fact(x)                  # fact function will give result
print(result)

