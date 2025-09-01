a = 1 ^ 0
b = 0 ^ 1
c = 0 ^ 0
d = 1 ^ 1
print(a, b, c, d)
print(bin(a), int(b), float(c), complex(d))

print("-"*50)

s1={1.2,2.3,4.5}
s2={2.3,4.5,6.5}
s3=s1^s2
print(s3)
a = {1.2,2.3,4.5}^{2.3,4.5,6.5}
print(a)

print("-"*50)

#b = 1.3 ^ 1.3 #TypeError: unsupported operand type(s) for ^: 'float' and 'float'
#print(b)
