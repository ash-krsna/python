#Program for swapping of any two numerical integer values --Logic-3
a,b = int(input("Enter Value of a:")),int(input("Enter Value of b:"))
print("-"*50)
print("\tOriginal val of a = {}".format(a))
print("\tOriginal val of a = {}".format(b))
print("-"*50)
a = a + b
b = a - b
a = a - b
print("\tSwapped value of a = {}".format(a))
print("\tSwapped value of b = {}".format(b))
print("-"*50)