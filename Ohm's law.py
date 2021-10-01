#Calculate Ohm's law

i= int(input("enter the value of current in amps : "))# i = current
v=int(input("enter the value of voltage in joules : ")) # v = voltage

#We know ohm's law is v=i*r or r=v/i
r = v/i
print(f"The respective resistance is {r} ohm")
