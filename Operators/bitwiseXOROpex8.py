lst1 = [10,20,30,40,50,60]
lst2 = [60,20,30,15,25,35,45]
try:
    a = lst1 | lst2
except TypeError:
    print("TypeError")
b = set(lst1)^set(lst2)
print(b)