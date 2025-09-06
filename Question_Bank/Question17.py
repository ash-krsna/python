#Python program to print odd number to n range
n = int(input("Enter Range:"))
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst[0:n]:
    if i % 2 !=0:
        print(i)
