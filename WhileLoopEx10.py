#write a python program which will generate all odd number in reverse order within given N range
n = int(input("Enter how many numbers you want to generate:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tOdd Numbers within:{}".format(n))
    print("-"*50)
    i = n
    while  i >= 1:
        if (i % 2 != 0):
            print("\t{}".format(i))
        i -= 1
