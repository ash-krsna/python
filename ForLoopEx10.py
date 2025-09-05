#program for calculating product of first n natural numbers
n = int(input("Enter how many numbers you want to generate:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tProduct of first {} natural numbers".format(n))
    print("-"*50)
    p = 1
    for i in range(1,n+1):
        print("\t{}".format(i))
        p=p*i
    else:
        print("-"*50)
        print("\tProduct of first {} natural numbers is:{}".format(n,p))
        print("-"*50)
