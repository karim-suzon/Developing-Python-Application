#User enters a weekday number and the program tells the name of the day

#viikko = ["Lauantai","Sunnuntai","Maanantai","Tiistai","Keskiviikko","Torstai","Perjantai"]


# Taken day number from user


viikko = int(input("Enter viikko päivä numero (1-7) : "))

if viikko == 1:
    print("\nMaanantai")

elif viikko == 2:
    print("\nTistai")

elif (viikko == 3):
    print("\nKeskivikko")

elif (viikko == 4):
    print("\nTorstai")

elif (viikko == 5):
    print("\nPerjantai")

elif (viikko == 6):
    print("\nLauantai")

elif (viikko == 7):
    print("\nSunnuntai")

else:
    print("\nPlease enter viikko numero between 1-7.")