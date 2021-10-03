#6 Convert seconds to hours, minutes, seconds


sec=int(input("enter time in second: "))
h=int(sec/3600)
sec=sec%3600
m=int(sec/60)
s=int(sec%60)

print("HH=MM=SS format ",h,":",m,":",s,":")
