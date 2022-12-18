def list_prdct(l1):
    result=1
    for i in l1:
        result=result*i
    return result

l1 =[]
x=int(input("enter how many elements you want :- "))
for i in range (x) :
    t=int(input(" enter the element  :- "))
    l1.append(t)

res = list_prdct(l1)
print(" product of the list elements :-  ",res)


