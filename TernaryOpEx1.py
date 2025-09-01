#write a program for accepting three numerical values and find min value and check for equality also
a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))
minvalue = "All Values are equal" if a == b == c else \
    ("a is min" if a>b and a<c else\
      ("b is min" if b >a and b<c else "c is min"))


print(minvalue)
