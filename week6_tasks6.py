#6.Returns the BMI.
name1 = "karim"
height_m1 = 1.65
weight_kg1 = 75

name2 = "suzon"
height_m2 = 1.8
weight_kg2 = 79

name3 = "abdul"
height_m3 = 1.72
weight_kg3 = 80

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg/(height_m**2)
    print("bmi: ")
    print(f"{bmi}")

    if bmi < 25:
        return name + "not overwight"
    else:
        return name + " is overwight"

result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)
print(f"{result1}")
print(f"{result2}")
print(f"{result3}")