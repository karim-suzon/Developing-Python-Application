#7. Convert euros to 5, 10, 20, 50, 100, 200, 500 euros bills



euros = [5, 10, 20, 50, 100, 200, 500]

for i in euros:
    if i % 5 == 0:
        print("These are bills : ",i, '£')

    else:
        print("by")
