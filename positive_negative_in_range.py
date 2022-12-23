start=int(input("enter the first number"))
stop=int(input("enter the second number"))
for i in range(start,stop+1):
    if i>0:
        print("positive",i,end=" ")
    elif i<0:
        print(i)