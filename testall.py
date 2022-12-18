print('''1.sum of natural number
2.even number 
3.odd number
4.prime number
5.factorial number''')
print("\nEnter Your Choice from the above list to get your pattern")
list = input("1,2,3,\t\t")
number=int(input("Enter number\t"))
if(list=="1"):
    if number < 0:
        print("Enter a positive number")
    else:
        sum = 0
        while (number > 0):
            sum += number
            number -= 1
        print("The sum is", sum)
elif(list=="2"):
    if (number % 2) == 0:
        print("The number is even")
    else:
        print("The number is odd")
elif(list=="3"):
    i = 2
    count = 0
    while (i < number):
        if (number % i == 0):
            n = 1
            break
        i = i + 1
    if (count == 1):
        print("number is not prime")
    elif (count == 0):
        print("no is prime")
        