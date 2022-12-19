# using reverse function
def reversing(l):
  l.reverse()
  return l
a = [23,34,33,23,233,44]  
print(reversing(a))

#using slicing
def reversing(l):
  l1 = l[::-1]
  return l1

a = [23,34,33,23,233,44]  
print(reversing(a))
