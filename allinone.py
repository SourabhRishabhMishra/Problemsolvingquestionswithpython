import sys
ch=int(sys.argv[1])
if ch==1:
    print("you choose , reverse number")
    rev=0
    while(rev<=ch):
        mod=mod%10
        rev=rev*10+mod
        ch=int(ch//10)
        print(rev)
if ch==2:
    print("you choose reverse string")
    n="Goourav srivastav" 
    print([:: -1]n)

if ch==3:
    print("you choose star 1 pattern")
    row=1
    while ch<=row:
        col=1
        while col<=ch:
            print("*",end=" ")
            col=col+1
        print()
        row=row+1

if ch==4:
    print("you choose 2 star pattern")
    row=1
    while row<=n:
        col=1
        while col<=ch:
            print("*",end=" ")
            col=col-1
        print()
        row=row+1
