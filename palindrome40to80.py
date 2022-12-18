a1=int(input(" enter the number 1 "))
a2=int(input(" enter the number 2 "))
res=0
while a1<=a2 :
    x=str(a1)
    rev=x[::-1]
    if a1==int(rev):
        res=res+a1
    a1=a1+1
print("your answer = ",res)    
