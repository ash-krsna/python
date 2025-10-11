#Write a python program for accepting Three numerical values and find min value and check for equaliy also.
a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))
minvalue = "All Value are Equal" if a == b == c else ("A is Min" if a<=b and a<=c else ("B is Min" if b <= a and b<=c else "C is Min"))
print("----------------")
print(minvalue)

