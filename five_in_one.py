print("1. even. ")
print("2. odd. ")
print("3. checking number is postive or negative. ")
print("4. checking ABC is valid triangle or not. ")
print("5. palindrome. ")

h=int(input("ENTER YOUR CHOICE. "))

if(h==1):
	print("YOU CHOOSE EVEN NUMBER. ")
	n=int(input("enter the value. "))
	i=2
	while(i<=n):
		print(i)
		i=i+2

if(h==2):
	print("YOU CHOOSE ODD  NUMBER. ")
	n=int(input("enter the value. "))
	i=1
	while(i<=n):
		print(i)
		i=i+2

if(h==3):
	print("YOU WANT TO CHECK NUMBER IS POSITIVE OR NOT. ")
	d=int(input("enter the value. "))
	if (d>0):
		print("number is positive. ")
	else:
		print("number is negative. ")

if(h==4):
	print("YOU WANT TO CHECK ABC IS VALID TRIANGLE OR NOT. ")
	a=int(input("enter the side 1 = "))
	b=int(input("enter the side 2 = "))
	c=int(input("enter the side 3 = "))
	if(a+b>c and b+c>a and c+a>b):
		print("ABC IS VALID TRIANGLE. ")
	else:
		print("ABC IS NOT VALID TRIANLE. ")

if(h==5):
	print("YOU CHOOSE PALINDROME. ")
	s=input("")
	revrse=s[::-1]
	if (revrse==s):
		print("IT IS PALINDRONME. ")
	else:
		print("IT IS NOT PALINDROME. ")








			







	







	