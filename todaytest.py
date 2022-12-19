import sys
n=len(sys.argv)
list=int(sys.argv[1])
number=int(input("Enter number\t"))
if(list==1):
    if(number%2==0):
        print("number is even")
    else:
        print("number is odd")

elif(list==2):
    fact= 1
    if (number < 0):
        print("enter a positive number")
    elif number == 0:
            print("The factorial of 0 is 1")
    else:
        for i in range(1, number + 1):
             fact= fact * i
        print("The factorial of", number, "is", fact)
elif(list==3):
    row = 1
    num1 = number
    while (row <= number):
        col = 1
        x = 1
        while (col <= num1):
            print(x, end=" ")
            col = col + 1
            x = x + 1
        num1 = num1 - 1
        while (col <= number):
            print("*", end=" ")
            col = col + 1
        stars2 = row - 1
        print()
        row = row + 1



