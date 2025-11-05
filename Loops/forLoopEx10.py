#Programming for calculating product of first n natural numbers.
n = int(input("Enter how many natural numbers product you want:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("First {} natural numbers".format(n))
    print("-"*50)
    p = 1 #mulplicative identity
    for i in range(1,n+1):
        print("\t{}".format(i))
        p = p * i
    else:
        print("-"*50)
        print("Product = {}".format(p))
        print("-"*50)