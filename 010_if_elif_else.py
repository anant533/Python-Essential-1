y=int(input("Enter the year : "))
if y<1582:
    print("not within gregorian ca;ender")
elif y%4 !=0:
    print("common year")

elif y%100 !=0:
    print("leap year")
elif y%400 !=0:
    print("common year")
else:
    print("leap year")
    
