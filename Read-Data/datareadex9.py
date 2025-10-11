#Program for cal simple interest and total amount to pay
p = float(input("Enter Principle Amount:"))
t = float(input("Enter Time:"))
r = float(input("Enter Rate of Interest:"))
#cal si
si = (p * t * r) / 100
#cal totamt
totamt = p + si
print("*"*40)
print("\t Principle Amount :",p)
print("\t Time : ",t)
print("\t Rate Interest :",r)
print("\t Simple Interest :",si)
print("\t Total Amount : ",totamt)
print("*"*40)

