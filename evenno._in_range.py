start=int(input("enter the first number"))
stop=int(input("enter the second number"))

        #even number
for i in range(start,stop,2):
    print(i)

for num in range(start,stop+1):
    if num%2==0:
        print(num,end=" ")

        #odd number
for num in range(start,stop+1):
    if num%2!=0:
        print(num,end=" ")
