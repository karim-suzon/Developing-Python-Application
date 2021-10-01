print("This program is to calculate the BMI of an induvidual\n")
name = input("Enter your name : ")
weight = float(input("pls enter your weight in kg : "))
height = float(input("pls inter your height in m : "))

bmi = weight/(height**2)

if bmi < 25:
    print(f"{name} is underweight by {bmi} BMI")

else:
    print(f"{name} is overweight by {bmi} BMI")