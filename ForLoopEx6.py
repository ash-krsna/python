#program for generating all even number in reverse order within the range N
n = int(input("Enter how many numbers you want to generate:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tEven Numbers within:{}".format(n))
    print("-"*50)
    if(n%2!=0):
        n=n-1
    for i in range(n,0,-2):
        print("\t{}".format(i))
    else:
        print("-"*50)
