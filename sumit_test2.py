import sys

ch = int(sys.argv[1])

if ch == 1:
  num1 = int(input("Enter num1:"))
  operator = int(input("Enter operator: 1.Addition 2.Subtraction 3.Division 4.Multiplication"))
  num2 = int(input("Enter num2:"))
  result = 0
  if operator == 1:
    result = num1 + num2
  if operator == 2:
    result = num1 - num2
  if operator == 3:
    result = num1 / num2
  if operator == 4:
    result = num1 * num2

  result2 = result
  print("The result is: ",result)
  repeat_choice = input("Want to perform again: y/n")
  if repeat_choice == 'y':
    while 1:
      num3 = int(input("Enter num3: "))
      operator = int(input("Enter operator: 1.Addition 2.Subtraction 3.Division 4.Multiplication"))
      if operator == 1:
        result2 = result2 + num3
      if operator == 2:
        result2 = result2 - num3
      if operator == 3:
        result2 = result2 / num3
      if operator == 4:
        result2 = result2 * num3
      print("The result is:",result2)

      repeat_choice = input(("Want to repeat again: y/n"))
      if repeat_choice == 'y':
        continue
      else:
        exit()
  else:
    exit()

if ch ==2 :
  n = int(input("Enter number: "))
  r = 1
  while r <=n:
    c = 1
    space = n - r
    x = 1
    while space:
      print(" ",end=" ")
      c = c + 1
      space = space - 1
    while c <= n:
      print(x,end=" ")
      c = c + 1
      x = x + 1
    y = 1
    z = r - 1
    while y < r:
      print(z,end=" ")
      y = y + 1
      z = z - 1
    print()
    r = r + 1