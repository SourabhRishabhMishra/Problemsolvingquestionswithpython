# Python program to demonstrate
# command line arguments


import sys

# total arguments
n = len(sys.argv)
print(n)
print(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
for a in range(1, n):
	print(sys.argv[a], end = " ")
	
# Addition of numbers
sourabh=''
print(type(sourabh))
# Using argparse module
for i in range(1, n):
	Sum += str(sys.argv[i])
	
print("\n\nResult:", Sum)
