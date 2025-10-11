#Program for swapping of any two numerical Integer values -- Logic-5
a,b = int(input("Enter Value of a:")),int(input("Enter Value of b:"))
print('-'*50)
print("\tOriginal val of a = {}".format(a))
print("\tOriginal val of b = {}".format(b))
print('-'*50)
a = a ^ b
b = a ^ b
a = b ^ a
print("\tSwapped value of a = {}".format(a))
print("\tSwapped value of b = {}".format(b))

