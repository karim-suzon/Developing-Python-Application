#Variables a, b, and c have different values. Create a program that finds the biggest one.Show 3 different ways to solve the problem.
#3rd example

a,b,c = int(input("1st value : ")), int(input("2nd value : ")), int(input("3rd value : "))

if a>b and b>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)