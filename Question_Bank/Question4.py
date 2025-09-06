#Python program to check if elements exists in a list.
#First Case
lst = [1,2,3,4,5]
a = "present in in the list" if 3 in lst else "not present in the list"
print(a)
print("-"*50)
#Second Case
n = int(input("Enter the number to be searched:"))
b = "present in the list" if n in lst else "not present in the list"
print(b)
print("-"*50)
#Third Case
lst = [1,2,3,4,5]
n = int(input("Enter the number to be searched:"))
c = print("{} Is present in the list".format(n)) if n in lst else print("{} is not present in the list".format(n))
print("-"*50)
