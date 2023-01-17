def fct(n):
    fact=1
    while(n!=1):
        fact=fact*n
        n=n-1
    return fact 
n=int(input("enter the number :- "))
res=fct(n)
print("YOUR FACTORIAL :-  ",res)