#Print this kind of semipyramid(character amount of rows is given in a variable)
# m
# mm
# mmm
# mmmm
# mmmmm
for i in range(5):
    for j in range(i+1):
        print("m", end="")
    print()