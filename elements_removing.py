def ele_rmv(l1):
    l2=[]
    w=int(input(" Enter thoose elements you do not want in your list :- "))
    for j in range(w):
        print(" Enter unwanted elements ",j+1,":-",end=" ")
        h=int(input())
        l2.append(h)
    l3 = []
    l3.extend(l1) # type of copying one list to another list 
    for ele in l1:
        if ele in l2:
            l3.remove(ele)
    return l3  
            
l1 = [] 
x=int(input(" enter how many elements you want to put in the list :- "))
for i in range(x):
    print(" enter element number ",i+1,":-",end=" ")
    n=int(input())
    l1.append(n) 
out = ele_rmv(l1)
print(out)