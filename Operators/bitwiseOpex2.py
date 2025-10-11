a = 10
b = a >> 3
print(b)
print(16 >> 2)
print(32 >> 3)
print(32 >> 2)
print(32 >> 0)
try:
    print(80.5 >> 4)
except TypeError:
    print("80.5 >> 4 --> TypeError")
try:
    print(42 >> -4)
except ValueError:
    print("42 >> -4 --> ValueError")
