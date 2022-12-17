a=int(input("enter the value "))
b=int(input("enter the value "))
c=int(input("enter the value "))
if a+b>c:
	if b+c>a:
		if c+a>b:
			print(" valid triangle ")
		else:
			print("invalid triangle")
		
	else:
		print("invalid triangle")

else:
	print("invalid triangle")
	
