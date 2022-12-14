print('''+ ADD 
- SUBTRACT 
/ DIVIDE 
* MULTIPLY''')
x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
operator = input(" +,-,/,* : ")
if(operator=="+"):
    print(x+y)
elif(operator=="-"):
    print(x-y)
elif(operator=="/"):
    print(x/y)
elif(operator=="*"):
    print(x*y)
else:
    print("Invalid input")