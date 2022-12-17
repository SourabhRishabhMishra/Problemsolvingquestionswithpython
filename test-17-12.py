import sys

n=int(sys.argv[1])

if n==1:
	num=int(input("enter the value "))
	fac=1
	while num>0:
		fac=fac*num
		num=num-1
	print("fac=" ,fac)
if n==2:
	num=int(input("enter the value "))
	z=1
	a1=0
	a2=1
	print(a1,"\n",a2)
	while z<=num:
		a3=a1+a2
		a1=a2
		a2=a3
		z=z+1
		print(a3)
if n==3:
	num=int(input("enter the value:- "))
	row=1
	while(row<=num):
		space=row-1
		while(space):
			print(" ",end=" ")
			space=space-1
		col=num-row+1
		while(col):
			print("*",end=" ")
			col=col-1
		print()
		row=row+1
	
	

	