i=0
while i<=100:
    print(i)
    i+=10  
    if i==60:
        print("Am I there")
        break    
print("the end")


n=int(input("enter the no : "))
print("the factors of ",n, "are:")
for i in range(1,n+1):
    if(n%i)==0:
        print(i,end=", ")
        
