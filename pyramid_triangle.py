'''n = int(input("enter the element :"))
k = 2*n-2
for i in range(0,n):
    for j in range (0,k):
        print(end="")
    k = k-2
    for j in range(0,i+1):
        print("*",end="")
    print()'''
# This is the example of print simple reversed right angle pyramid pattern
'''rows = int(input("Enter the number of rows:"))
k = 2 * rows - 2  # It is used for number of spaces
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2   # decrement k value after each iteration
    for j in range(0, i + 1):
        print("* ", end="")  # printing star
    print("")'''

n = 5

k = n - 1    # number of spaces
 
for i in range(0, n):
     
        
       
    for j in range(0, k):# inner loop to handle number spaces
            print(end=" ") # values changing acc. to requirement
     
        
    k = k - 1# decrementing k after each loop
     
        
        
    for j in range(0, i+1):# inner loop to handle number of columns
         # values changing acc. to outer loop
            # printing stars
            print("* ", end="")
     
       
    print("\r") # ending line after each row
 

