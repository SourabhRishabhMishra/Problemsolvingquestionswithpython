def largest(l):
  l.sort()
  return l[-1] 

l1= []  

a = int(input("how many element you want in list:"))  
for i in range (a):
  b = int(input("enter the element:"))
  l1.append(b)
res = largest(l1) 
print(res)  