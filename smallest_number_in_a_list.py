def smallest_num(l):
  l.sort()
  return l[0]
l1 = []  

a = int(input("how many element you want in list:"))  
for i in range (a):
  b = int(input("enter the element:"))
  l1.append(b)
res = smallest_num(l1) 
print(res)  