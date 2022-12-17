import sys
num = (sys.argv[1])

if num == 1:
 a = int(input("enter the number to check its palindrome"))
 l1 = [a]
 l1 = [::-1]
 if a == a:
    print("its palindrome")
 else:
    print("its not a palindrome")  
if num == 2:
  n = 5
  r = 1
  while r<=n:
    space = n - r
    c = 1
    count  = r 
    while space:
      print(" ",end="")
      space = space - 1
      c = c + 1
    while c<=r:
      print(count,end=" ")
      count = count + 1
      c = c + 1
    print()
    r = r+1
if num == 3:
  n = 5
  r = 1
  while r<=n:
    space = r - 1
    c = 1
    count  = r 
    while space:
      print(" ",end="")
      space = space - 1
      c = c + 1
    while c<=r:
      print(count,end=" ")
      count = count + 1
      c = c + 1
    print()
    r = r+1

    