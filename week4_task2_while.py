#Program calculates the sum of even numbers between 2-40.
#Use:while loop

maximum = int(input(" Please Enter the Maximum Value 40 : "))
sum = 0
number = 1

while number <= maximum:
    if (number % 2 == 0):
        print(number)
        sum = sum + number
    number = number + 1

print("The Sum of Even Numbers from 2 to 40 = ", sum)