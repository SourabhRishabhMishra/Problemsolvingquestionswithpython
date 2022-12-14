n=int(input("Enter number"))
row=1
while(row<=n):
    space=n-row
    while(space):
        print(end=" ")
        space = space - 1
    col=1
    while(col<=row):
        print("*",end=" ")
        col=col+1
    print()
    row=row+1