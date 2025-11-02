#Write a python program which will generate all the odd numbers in reverse order within given n range
n = int(input("Enter Range:"))
if n <= 0:
    print("\t\t{}is invalid input".format(n))
else:
    print("-"*50)
    print("\t\tOdd numers within:{}".format(n))
    print("-"*50)
    i = n
    while i >= 1:
        if i % 2 != 0:
            print("\t\t{}".format(i))
        i -= 1
