num = int(input("enter number:"))
r = 1
num1 = num
while r <= num:
  c = 1
  x = 1
  while c<=num1:
    print(x,end="")
    x = x+1
    c = c+ 1
  num1 = num1  - 1  
  
  while c<=num:
    print("*",end="")
    c = c+ 1

  stars2 = r - 1
  while stars2:
    print("*",end="")  
    stars2 = stars2 - 1
    c = c + 1
     
  y = num - r + 1
  while y:
    print(y,end="")   
    y = y - 1
    c = c + 1
  print()  
  r = r+1