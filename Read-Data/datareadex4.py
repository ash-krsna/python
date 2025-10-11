#Program for accepting two numerical values and find their product
print("Enter Two Numerical Values:")
x = input()
y = input()
#Convert x and y Values in int type
a = float(x)
b = float(y)
#find product
c = a * b
#display the result
print("-"*50)
print("Product({},{})={}".format(a,b,c))
print("-"*10 and "OR" and "-"*10)
print("Product(%0.2f,%0.2f) = %0.2f"%(a,b,c))
print("-"*10 and "OR" and "-"*10)
print("Product({},{})={}".format(round(a,2),round(b,2),round(c,2)))
print("-"*50)
