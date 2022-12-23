list1 = [10, 21, 4, 45, -66, 93, -1]
postive_count=0
negative_count=0
for num in list1:
    if num>0:
        postive_count +=1
    else:
        negative_count+=1
print("postive numbers",postive_count)
print("negative numbers",negative_count)
