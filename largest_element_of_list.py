def largest_element_of_list(l1):
   l1.sort()
   return l1[-1]

l1 = []
x=int(input("enter how many elements you want :- "))
for i in range (x) :
    t=int(input(" enter the element  :- "))
    l1.append(t)

res = largest_element_of_list(l1)
print(" product of the list elements :-  ",res)


