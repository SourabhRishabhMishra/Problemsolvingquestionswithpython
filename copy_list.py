# def cloning_list(l1):
#     list_copy=l1[ : ]
#     return list_copy
# l1=["gourav",9311340498,"asus","india",3456,"thtt"]
# l2=cloning_list(l1)    #copying L1 into L2
# print("l2 after cloning/copying  --->",l2)

# import copy
# l1=["gourav",9311340498,"asus","india",3456,"thtt"]
# l2=copy.copy(l1)
# print(l2)

def cloning_list(l1):
    list_copy=[]
    for item in l1: list_copy.append(item)
    return list_copy
l1=["gourav",9311340498,"asus","india",3456,"thtt"]
l2=cloning_list(l1)
print(l2)