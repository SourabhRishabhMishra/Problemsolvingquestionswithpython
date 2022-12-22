def odd_num(l1):
    l2 = []
    for i in l1 :
        if i % 2 == 1 :
            l2.append(i)
    return l2

l1 = []
x = int(input("Enter how many elements you want to put in the list :- "))
for i in range (x):
    print("Enter the element",i+1,":-",end=" ")
    n=int(input())
    l1.append(n)
output = odd_num(l1)
print("Your odd list :- ",output)