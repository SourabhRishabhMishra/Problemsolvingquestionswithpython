print('''1.Square Star Pattern  
2.Row Number Square Pattern
3.Column Square Pattern
4.Natural no Square Pattern
5.Star Pyramid Square Pattern
6.Right Triangle Star Pattern 
7.Right Triangle column Pattern
8.Single Alphabet in one line Square Pattern
9.Alphabet Square Pattern
10.Alphabet Triangle Square Pattern
11.complex pattern''')
print("\nEnter Your Choice from the above list to get your pattern")
list = input("1,2,3,4,5,6,7,8,9,10,11\t\t")
number=int(input("Enter number\t"))
if(list=="1"):
    row = 1
    while (row <= number):
        col = 1
        while (col <= number):
            print("*", end=" ")
            col = col + 1
        print()
        row = row + 1
elif(list=="2"):
    row = 1
    while (row <= number):
        col = 1
        while (col <= number):
            print(row, end=" ")
            col = col + 1
        print()
        row = row + 1
elif(list=="3"):
    row = 1
    while (row <= number):
        col = 1
        while (col <= number):
            print(col, end=" ")
            col = col + 1
        print()
        row = row + 1
elif(list=="4"):
    row = 1
    i = 1
    while (row <= number):
        col = 1
        while (col <= number):
            print(i, end=" ")
            col = col + 1
            i = i + 1
        print()
        row = row + 1
elif(list=="5"):
    row = 1
    while (row <= number):
        space = number - row
        while (space):
            print(end=" ")
            space = space - 1
        col = 1
        while (col <= row):
            print("*", end=" ")
            col = col + 1
        print()
        row = row + 1

elif (list == "6"):
    row = 1
    while (row <= number):
        col = 1
        while (col <= row):
            print("*", end=" ")
            col = col + 1
        print()
        row = row + 1
elif (list == "7"):
    row = 1
    while (row <= number):
        col = 1
        while (col <= row):
            print(col, end=" ")
            col = col + 1
        print()
        row = row + 1
elif (list == "8"):
    row = 1
    i = 64
    while (row <= number):
        i = i + 1
        col = 1
        while (col <= number):
            print(chr(i), end=" ")
            col = col + 1
        print()
        row = row + 1
elif (list =="9"):
    row = 1
    i = 1
    while (row <= number):
        col = 1
        while (col <= number):
            print(chr(64 + i), end=" ")
            i = i + 1
            col = col + 1
        print()
        row = row + 1
elif(list=="10"):
    row = 1
    while (row <= number):
        col = 1
        while (col <= row):
            print(chr(65 + col + row - 2), end=" ")
            col = col + 1
        print()
        row = row + 1
elif(list=="11"):
    r = 1
    num1 = number
    while (r <= number):
        c = 1
        x = 1
        while (c <= num1):
            print(x, end=" ")
            c = c + 1
            x = x + 1
        num1 = num1 - 1
        while (c <= number):
            print("*", end=" ")
            c = c + 1
        stars2 = r - 1
        while (stars2):
            print("*", end=" ")
            stars2 = stars2 - 1
            c = c + 1
        y = number - r + 1
        while (y):
            print(y, end=" ")
            y = y - 1
            c = c + 1
        print()
        r = r + 1
else:
    print("Invalid input")