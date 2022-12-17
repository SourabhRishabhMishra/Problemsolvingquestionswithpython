p=print("1st star pattern")
p=print("2nd no. pattern")
p=print("3rd char pattern")

h=int(input("enter your choice"))
if h==1:
 print("you choose, star pattern")
n=int(input("enter the value"))
row=1
while(row<n):
    col=1
    while(col<=row):
        print("*",end=" ")
        col=col+1
    print()
    row=row+1

if h==2:
    print("you choose,no.pattern")
    n=int(input("enter the value"))
    row=1
    count=1
    while(row<=n):
        col=1
        while col<=row:
            print(count,end=" ")
            count=count+1
            col=col+1
        print()
        row=row+1

if h==3:
   n=int(input("enter the value"))
row=1
x=1
while(row<=n):
    col=1
    while(col<=n):
        print(chr(64+x),end=" ")
        x=x+1
        col=col+1
    print()
    row=row+1   
 


