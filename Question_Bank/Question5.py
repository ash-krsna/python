#Different ways to clear a list in Python.
#First Case
lst = [1,2,3,4,5]
print("Length of the list is:",len(lst))
print("After clearing the list:")
a = lst.clear()
print("Length of the list is:",a)
#Second Case
lst1 = [1,2,3,4,5]
print("Length of the list is:",len(lst1))
print("After clearing the list:")
for i in range(len(lst1)):
    lst1.pop()
print("Length of the list is:",len(lst1))
