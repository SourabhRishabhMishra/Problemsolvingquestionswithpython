def smallest_digit(l1):
    l1.sort()
    return l1[0]

l1 = []
x=int(input(" enter how many elements you want to put in the list :- "))
for i in range(x):
    n=int(input(" enter the element :-"))
    l1.append(n)

rslt = smallest_digit(l1)
print(rslt)