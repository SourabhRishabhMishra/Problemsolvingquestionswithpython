a = int(input("enter the variable:"))
b = int(input("enter the variable:"))
final_sum = 0
while a<=b:
  x = str(a)
  rev = x[::-1]
  if a == int(rev):
    final_sum = final_sum+a
  a = a + 1
print("final sum:",final_sum)    