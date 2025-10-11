#Python program to interchange first and last elements in a list
a = [1,2,3,4,5,6]
print(a)
a[-1],a[0] = a[0],a[-1]
print(a)

