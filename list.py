list = int(input( "Enter number : "))
mylist=[11,15,7,19]
if(list==1):
    print(mylist)
    pos1,pos2=1,3
    mylist[pos1],mylist[pos2]=mylist[pos2],mylist[pos1]
    print(mylist)
elif(list==2):
    print(mylist)
    pos1,pos2=1,3
    temp=mylist.pop(pos1)
    x=mylist.pop(pos2-1)

    mylist.insert(pos1,x)
    mylist.insert(pos2,temp)
    print(mylist)
elif(list==3):
    print(mylist)
    pos1,pos2=1,3
    get=(mylist[pos1]),(mylist[pos2])
    mylist[pos2],mylist[pos1]=get
    print(mylist)