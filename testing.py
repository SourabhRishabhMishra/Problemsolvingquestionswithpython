p=print("prime no.")
p=print("even odd")
p=print("star pattern")
p=print("pattern")

h=int(input("enter your choice"))
if h==1:
n=int(input(enter the value))
i = 2
count =1
 while (i < number):
        if (number % i == 0):
            n = 1
            break
        i = i + 1
    if (count == 1):
        print("number is not prime")
    elif (count == 0):
        print ("no is prime")=1

if h==2:
n=int(input("enter the value"))
if n%2==0:
    print("num is even")
else:
    print("num is odd")

if h==3:
 num=int(input("enter the value:- "))
row=1
while(row<=num):
	space=num-row
	while(space):
		print(" ",end=" ")
		space=space-1
	col=1
	while(col<=row):
	      print("*",end=" ")
	      col=col+1
	print()
	row=row+1

    


