print(796/60)
print(796//60)
print(796%60)


H1=int(input("Start time in hours: "))
M1=int(input("start time in minutes: "))
d=int(input("Time duration in minutes: "))
F=H1*60+M1+d
H2=F//60
M2=F-H2*60
print("The finish time is = ",H2,":",M2)
