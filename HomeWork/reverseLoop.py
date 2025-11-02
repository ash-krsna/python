n = int(input("Enter Range:"))
if n <= 0:
    print("\t\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\t\tEven numbers within:{}".format(n))
    print('-'*50)
    i = n
    while (i >= 1):
        if i % 2 == 0:
            print("\t\t{}".format(i))
        i = i - 1