a = {1.2,2.3} ^ {1.2,2.3}
b = 123 ^ 123
print(a)
print(b)
try:
    b = 1.2 ^ 1.2
except TypeError:
    print("TypeError")