#write a python program which will generate all the odd number withing the given range N
n = int(input("Enter how many numbers you want to generate:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tOdd Numbers within:{}".format(n))
    print("-"*50)
    i = 1
    while  i <= n:
        if (i % 2 != 0):
            print("\t{}".format(i))
        i += 1
