# Take three values from user and find the greatest number from them

#a, b, c= int(input('enter first number')), int(input('enter second number')), int(input('enter third number'))
#nums= [a, b, c]
#print(max(nums))

#x,y,z = int(input("1st num")),int(input("2nd num")),int(input("3rd num"))
#if x>y and x>z :
    #print(x)
#elif y>z:
    #print(y)
#else :
    #print(z)




#User gives a value and our program tells if the value is > 100 or not

user_number = int(input("pls enter a value : "))


if user_number > 100:
    print("value is greater than 100,", 'input number is : ',user_number)
elif user_number == 100:
    print("value is equal",user_number)
else:
    print("the value is less than 100,", 'input number is : ',user_number)


