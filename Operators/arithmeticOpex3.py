#Program for calculate square root of a given number without using sqrt() of math module
n = float(input("Enter Value of n:"))
sqrtv = n ** 0.5 # or sqrtv = n ** (1/2)
print("----------------OR--------------")
print("sqrt({})={}".format(n,round(sqrtv,2)))