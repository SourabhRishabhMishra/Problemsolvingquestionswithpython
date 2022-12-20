n = int(input(" Enter the Number "))
row = 1
while(row<=n):
	column = 1
	while(column<=n):
		print("*",end=" ")
		column = column+1
	print()
	row=row+1