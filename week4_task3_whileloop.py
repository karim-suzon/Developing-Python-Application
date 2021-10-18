#Program calculates sum: 5, 10, 15,..100.
#while loop


print(list(range(5,101,5)))

max_val = int(input(" Please Enter the Maximum Value 100 : "))

sum = 0
number = 1
while number <= max_val:
    if number % 5 == 0:
        sum = sum + number
    number+= 1
print("sum of those numbers : ", sum)
