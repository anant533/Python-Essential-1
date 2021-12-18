x=float(input("Enter your income:"))
if x<85528:
    tax=(0.18*x)-556.02
    if tax<=0:
        tax=0
    print("This is your tax ",tax,"amount to be paid")
else:
    tax=14839+(0.32*(x-85528))
    print("This is your tax ",tax,"amount to be paid")
    
