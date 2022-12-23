list=[2,3,4,5,6,7,0,5,99]
# del list[1:6]                  #using del()
# print(list)

for i in list:                   #iterate each value
    if i%2==0:
        list.remove(i)           #remove() remove all even numbers from list
print(list)