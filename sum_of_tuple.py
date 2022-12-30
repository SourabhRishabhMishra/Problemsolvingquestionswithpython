def sum(l1):

	t1 = list(l1)

	
	count = 0
	for i in t1:
		count = count + i
	return count

t1 = (5, 20, 3, 7, 6, 8)

print(sum(t1))