#Program calculates the sum of even numbers between 2-40.
#Use:for loop

sum = 0
for i in range(2, 40):
    if i%2 == 0:
        sum = sum + i
        print("The even numbers are : ", i)
print("The sum of even numbers : ", sum)
