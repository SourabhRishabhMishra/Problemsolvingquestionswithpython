n = int(input("enter the element:"))
row = 1
while row<=n:
  col = 1
  count = 1
  space = n - row
  while space:
    print(" ",end="")
    space = space - 1
  while col<=row:
    print("*",end="")
    count = count + 1
    col = col + 1
  y = row - 1
  while y:
    print("*",end="")
    y  = y - 1
  row = row + 1
  print()  