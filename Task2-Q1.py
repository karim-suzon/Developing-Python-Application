#User gives a value and our program tells if the value is > 100 or not

user = int(input("pls enter a value : "))


if user > 100:
    print("value is greater than 100,", 'input number is : ',user)
elif user == 100:
    print("value is equal",user)
else:
    print("the value is less than 100,", 'input number is : ',user)