#program for generating n to 1
n = int(input("Enter how many numbers you want to generate:"))
if(n<0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tNumbers within:{}".format(n))
    print("-"*50)
    for i in range(n,0,-1):
        print("\t{}".format(i))
    else:
        print("-"*50)
