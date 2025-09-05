#program for calculating sum of first n natural numbers
n = int(input("Enter how many numbers you want to generate:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tSum of first {} natural numbers".format(n))
    print("-"*50)
    p = 0
    i=1
    while(i<=n):
        print("\t{}".format(i))
        p=p+i
        i+=1
    else:
        print("-"*50)
        print("\tSum of first {} natural numbers is:{}".format(n,p))
        print("-"*50)
