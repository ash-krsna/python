#Different ways to clear a list in Python
a =[2,3,44,8,66,56,4,90,76,45,3,7,5,92]
print("Before a",a)
a.clear()
print("After clearing a",a)


print("-"*50)
b = [2,3,44,8,66,56,4,90,76,45,3,7,5,92]
print("Before",b)
while b:
    b.pop()
print("After",b)