#Program calculates sum: 5, 10, 15,..100.
#for loop

sum = 0
for i in range(5,100):
    if i % 5 == 0:
        print("numbers are = ", i)
        sum = sum + i
print("sum of those numbers : ", sum)