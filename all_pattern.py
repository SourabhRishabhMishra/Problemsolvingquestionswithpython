"""print("1. SIMPLE STAR PATTERN (R*C). ")
print("2. SIMPLE NUMBER PATTERN . ")
print("3. SIMPLE NATURAL NUMBER PATTERN .  ")
print("4. SIMPLE NUMBER RIGHT ANGLE TRIANGLE PATTERN . ")
print("5. NATURAL NUMBER RIGHT ANGLE TRIANGLE PATTERN .")
print("6. RIGHT ANGLE  TRIANGLE PATTERN [INCERMENT IN THE ROW] . ")
print("7. RIGHT ANGLE  TRIANGLE PATTERN [DECREMENT IN THE ROW] .")
print("8. RIGHT ANGLE  TRIANGLE PATTERN [BY USING ASCII VALUE ] .")
print("9. LEFT SIDE RIGHT ANGLE TRIANGLE STAR[*] PATTERN .")
print("10.INVERTED RIGHT ANGLE TRIANGLE STAR PATTERN .")
print("11.INVERTED MIRRORED RIGHT ANGLE TRIANGLE STAR PATTERN . ")
print("12.LEFT SIDE RIGHT ANGLE TRIANGLE [ACCORDING TO THE ROW] .")
"""

import sys

print("File name: ",sys.argv[0])


h = int(sys.argv[1])


if h==1 :
	print("YOU CHOOSE SIMPLE STAR PATTERN (R*C) . ")
	n = int(input(" Enter the Number "))
	row = 1
	while(row<=n):
		column = 1
		while(column<=n):
			print("*",end=" ")
			column = column+1
		print()
		row=row+1
if h==2 :
	print("YOU CHOOSE SIMPLE NUMBER PATTERN . ")
	n=int(input("enter the num. "))#5
	row=1
	while(row<=n):
		col=1
		while(col<=n):
			print(row,end=" ")
			col=col+1
		print()
		row=row+1
if h==3 :
	print("YOU CHOOSE SIMPLE NATURAL NUMBER PATTERN . ")
	n=int(input("enter the value"))
	count = 1
	row = 1
	while(row<=n):
		col= 1
		while(col<=n):
			print(count,end=" ")
			count = count+1
			col = col+1
		print()
		row = row+1
if h==4 :
	print(" YOU CHOOSE SIMPLE NUMBER RIGHT ANGLE TRIANGLE PATTERN .")
	n = int(input("enter the value"))
	row = 1
	while(row<=n):
		col = 1
		while(col<=row):
			print(col,end=" ")
			col=col+1
		print()
		row=row+1
if h==5 :
	print(". YOU CHOOSE NATURAL NUMBER RIGHT ANGLE TRIANGLE PATTERN . ")
	n=int(input("Enter number.  "))
	row = 1 
	count = 1
	while(row<=n):
		col=1
		while(col<=row):
			print(count,end=" ")
			count=count+1
			col=col+1
		print()
		row=row+1
if h==6 :
	print(" YOU CHOOSE RIGHT ANGLE  TRIANGLE PATTERN [INCREMENT IN THE ROW] . ")
	n=int(input("enter number. "))
	row=1
	while(row<=n):
		value=row
		col=1
		while(col<=row):
			print(value , end=" ")
			value=value+1
			col=col+1
		print()
		row=row+1
if h==7 :
	print(" YOU CHOOSE RIGHT ANGLE  TRIANGLE PATTERN [DECREMENT IN THE ROW] .")
	n=int(input("enter the value."))
	row=1
	while(row<=n):
		col=1
		while(col<=row):
			print(row-col+1,end=" ")
			col=col+1
		print()
		row=row+1
if h==8 :
	print(" YOU CHOOSE RIGHT ANGLE  TRIANGLE PATTERN [BY USING ASCII VALUE ] .")
	n=int(input("enter the value:- "))
	row=1
	while(row<=n):
		col=1
		while(col<=row):
			print(chr(65+row+col-2),end=" ")
			col=col+1
		print()
		row=row+1
if h==9 :
	print(" YOU CHOOSE LEFT SIDE RIGHT ANGLE TRIANGLE STAR[*] PATTERN . ")
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
if h==10 :
	print("YOU CHOOSE INVERTED RIGHT ANGLE TRIANGLE STAR PATTERN . ")
	num=int(input("enter the value:- "))
	row=1
	while(row<=num):
		space=num-row+1
		while(space):
			print("*",end=" ")
			space=space-1
		print()
		row=row+1
if h==11 :
	print(" YOU CHOOSE INVERTED MIRRORED RIGHT ANGLE TRIANGLE STAR PATTERN .  ")
	num=int(input("enter the value:- "))
	row=1
	while(row<=num):
		space=row-1
		while(space):
			print(" ",end=" ")
			space=space-1
		star=num-row+1
		while(star):
			print("*",end=" ")
			star=star-1
		print()
		row=row+1
if h==12 :
	print(" YOU CHOOSE LEFT SIDE RIGHT ANGLE TRIANGLE [ACCORDING TO THE ROW] . ")
	n=int(input("Enter The Value:- "))
	row=1
	while(row<=n):
		space=n-row
		while(space):
			print(" ",end=" ")
			space=space-1
		x=1
		column=1
		while(column<=row):
			print(row,end=" ")
			column=column+1
		print()
		row=row+1	




	










































