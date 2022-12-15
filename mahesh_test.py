import sys

ch = ("1","2","3","4")
num = sys.argv
if num == "1":
  r = 1
  while r<=5:
    c = 1
    space = num - r
    while space:
      print(" ",end="") 
      space = space - 1
      col = col + 1
    while c<=num:
      print("*",end="")
      c = c + 1
    print()
    r = r + 1   
if num == "2":
  r = 1
  while r<=5:
    c = 1
    count = 45
    space = num - r
    while space:
      print(" ",end="") 
      space = space - 1
      col = col + 1
    while c<=num:
      print(count,end="")
      count = count + 1
      c = c + 1
    print()
    r = r + 1
if num == "3" :
  r = 1
  while r<=5:
    c = 1
    count = 45
    
    while c<=r:
      print(count,end="")
      count = count + 1
      c = c + 1
    print()
    r = r + 1  
if num == "4" :   
  r = 1
  while r<=5:
    c = 1
    count = 45
    space = num - r
    while space:
      print(" ",end="") 
      space = space - 1
      col = col + 1
    while c<=num:
      print(count,end="")
      count = count + 1
      c = c + 1
    print()
    r = r + 1       