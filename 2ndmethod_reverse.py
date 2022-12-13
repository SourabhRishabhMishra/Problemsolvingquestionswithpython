p = print("1st method")
p = print("2nd method")
p = print("3rd method")
p = print("4th star pattern")

h = int(input("enter your choice"))
if h == 1:
    print("you choose ,1st method")
    n = "hello gourav"[::-1]
    print(n)
    
if h == 2:
    print("you choose ,2nd method")

    def reverse(s):
        if len(s) == 0:
            return s
        else:
            return reverse(s[1:]) + s[0]
s = "Gourav srivastav"
print("The original string is : ", end="")
print(s)
print("The reversed string(using recursion) is : ", end="")
print(reverse(s))

if h == 3:
    print("you choose ,3rd method")

    def reverse(s):
        str = ""
        for i in s:
            str = i + str
            return str

s = "Gourav srivastav"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))

if h==4:
    print("you choose ,star pattern")
    def pattern(n): 
        i = 1
        while i<=n:
            print(" "*(n-i) + "*" * i)
            i+=1 
            n = int(input('Enter the number of rows: '))
            pattern(n)