a = 10
b = a << 3
print(b)
print(4 << 3)
print(9 << 2)
print(10 << 0)
try:
    print(10.3 << 2)
except TypeError:
    print("10.3 << 2 --> TypeError")
try:
    print(4 << -1)
except ValueError:
    print("4 << -1 --> ValueError")


