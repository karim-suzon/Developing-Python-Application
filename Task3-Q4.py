#User gives a month number and our program tells the number of days in that month
#30 ("April", "June", "September", "November"):
# 31 ("January", "March", "May", "July", "August", "October", "December"):

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = int(input("Input the number of a Month (1-12) : "))

if month_name == 1:
    print("No. of days : 31 ,", 'Month name is : January')
elif month_name == 2:
    print("No. of days: 28/29 ,", 'Month name  : February')
elif month_name == 3:
    print("No . of days : 31 ,", 'Month name : March')
elif month_name == 4:
    print("No. of days: 30 ,", 'Month name  : April')
elif month_name == 5:
    print("No. of days: 31 ,", 'Month name : May')
elif month_name == 6:
    print("No . of days: 30 ,", 'Month name : June')
elif month_name == 7:
    print("No . of days : 31 ,", 'Month name : July')
elif month_name == 8:
    print("No . of days : 31 ,", 'Month name : August')
elif month_name == 9:
    print("No . of days : 30 ,",'Month name : September')
elif month_name == 10:
    print("No. of days : 31 ,", 'Month name : October')
elif month_name == 11:
    print("No. of days : 30 ,", 'Month name : November')
elif month_name == 12:
    print("No. of days : 31 ,", 'Month name : December')
else:
    print("Wrong month name")