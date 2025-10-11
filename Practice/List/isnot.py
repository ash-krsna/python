#Python | Ways to check if element exists in list
a=[2,3,4,5,6,5,6,55,4,3,4,3,87,9,809,89,90,67,5]
print("-"*50)
b = int(input("Enter number:"))
if b not in a:
    print("False")
else:
    print("True")