#Write a python program which will generate all the odd numbers within the given range N
n = int(input("Enter Range:"))
if n <= 0:
    print("\t\t{}is invalid input".format(n))
else:
    print("-"*50)
    print("\t\tOdd numers within:{}".format(n))
    print("-"*50)
    i = 1
    while i <= n:
        if i % 2 != 0:
            print("\t\t{}".format(i))
        i += 1
