#7. Convert euros to 5, 10, 20, 50, 100, 200, 500 euros bills

acc = int(input("Input your amount of money: "))

fh = int(acc // 500)

fh1 = int(acc % 500)

th = int(fh1 // 200)

th1 = int(fh1 % 200)

oh = int(th1 // 100)

oh1 = int(th1 % 100)

ft = int(oh1 // 50)

ft1 = int(oh1 % 50)

tt = int(ft1 // 20)

tt1 = int(ft1 % 20)

ten = int(tt1 // 10)

ten1 = int(tt1 % 10)

fi = int(ten1 // 5)

fi1 = int(ten1 % 5)

print("The number of bank notes converted: ", fh, "500e notes", th, "200e notes", oh, "100e notes", ft, "50e notes", tt, "20e notes", ten, "10e notes", fi, "5e notes")