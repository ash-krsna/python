lst1 = [10,"RS",True]
print(lst1,id(lst1))
lst2 = lst1 #deep copy
print(lst2, id(lst2))
a = lst1 is lst2
print("lst1 is lst2 =>",a)
b = lst1 is not lst1
print("lst1 is not lst2 =>",b)
lst1 = [10,"RS",True]
print(lst1,id(lst1))
lst2 = lst1.copy()
print(lst2,id(lst2))
a = lst1 is lst2
print(a)
b = lst1 is not lst2
print(b)

