def interchange(l):
  l[0],l[-1] = l[-1],l[0]
  return l

a = [20,30,40,50,30]  
print(interchange(a))