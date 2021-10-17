#User gives a value and our program tells if the value is > 100 or not

user_number = int(input("pls enter a value : "))


if user_number > 100:
    print("value is greater than 100,", 'input number is : ',user_number)
elif user_number == 100:
    print("value is equal",user_number)
else:
    print("the value is less than 100,", 'input number is : ',user_number)


