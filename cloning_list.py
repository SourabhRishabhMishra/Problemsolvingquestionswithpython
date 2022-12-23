l1 = []
x=int(input("enter how many elements you want to put in your list :- "))
for i in range(x):
    print("enter the element",i+1,":-",end=" ")
    element = int(input())
    l1.append(element)
'''l2=[]
l2.extend(l1)
print("Your cloned list = ",l2)'''
#     OR
l2 =[]
l2 = l1
print("Your copied list = ",l2)
    


