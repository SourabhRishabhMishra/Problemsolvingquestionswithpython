# LONGEST COMMON PREFIX

L1=['geek','geeks','geezier']
m=len(L1)
L1.sort()
end=min(len(L1[0]),len(L1[m-1]))
i=0
while(i<end and L1[0][i]==L1[m-1][i]):
	i=i+1
x=L1[0][0:i]
print(x)



