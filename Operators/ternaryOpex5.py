#Write a Python program which will accept Three Numerical Value and find Max Vallue and check Equality also.
n1 = float(input("Enter First Numerical Value:"))
n2 = float(input("Enter Second Numerical Value:"))
n3 = float(input("Enter Third Numerical Value:"))
maxval = n1 if n1 >= n2 and n1 > n3 else n2 if n2>n1 and n2>=n3 else n3 if n3>=n1 and n3>n2 else "All Values are equal"
print("Max({}, {}, {}) = {}".format(n1,n2,n3,maxval))