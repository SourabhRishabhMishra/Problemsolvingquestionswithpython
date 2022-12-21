def rmv_multiple_ele(l1):
# l1=[1,2,3,4,5]  , l2=[3,4]
    l2=[]
    z=int(input(" enter how many elements you do not  want to put in the list :- "))
    for j in range(z):
        print(" enter element you do not want number ",j+1,":-",end=" ")
        m=int(input())
        l2.append(m)
    l3 = []
    l3.extend(l1) # type of copying one list to another list 
    for ele in l1:
        if ele in l2:
            print("remove elememnt :- ",ele)
            l3.remove(ele)
            print("new value of l3 :- ",l3)
    return l3  
            
l1 = [] 
x=int(input(" enter how many elements you want to put in the list :- "))
for i in range(x):
    print(" enter element number ",i+1,":-",end=" ")
    n=int(input())
    l1.append(n) 


out = rmv_multiple_ele(l1)
print(out)
























'''l1 = [1,2,3,4,5,6] 
print("before")
print(l1)
l2 = [4,5]
for i in l1:
    for j in l2:
        if l1[i] in l2[j]:
            del i
print("after")
print(l1) '''