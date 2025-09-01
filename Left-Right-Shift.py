import os
a = 5
b = a<<1
c = a << 2
print("Left << shift Operator")
print(b,"\n",c)
d = a >> 1
e = a >> 2
print("_"*50, "\n")
print("Right >> shift Operator")
print(d,os.linesep, e)
ds= ~101
print(ds)
p = 0b110 ^ 0b111
q = 0b110 | 0b111
r = 0b110 & 0b111
print("--"*30)

print(p,os.linesep,q,os.linesep,r,)

print("_"*20)
x = 5
print(-(~x))

print("_"*20)
print("_"*20)
a = 4
b = 6
print(a^b)

a1= (a&b) & (~a | ~b)
a2 = (a|b) & (~a | ~b)
a3 = (a | a) & (~b | ~b)

print(a1,os.linesep, a2, os.linesep, a3)

print("_"*20)
print("_"*20)

n1 = 2
n2 = 3
#print(bin(n1) & bin(n2))

ab = 0b111>>2
print(ab)
print("_"*20)
b1 = -4^5
b2 = -6^-5
b3 = ~-10

print(b1,os.linesep, b2, os.linesep, b3)
