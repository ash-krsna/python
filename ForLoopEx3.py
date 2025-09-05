#program for generating all even numbers within in N where N is +ve
n = int(input("Enter how many numbers you want to generate:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tEven Numbers within:{}".format(n))
    print("-"*50)
    for i in range(2,n+1,2):
        print("\t{}".format(i))
    else:
            print("-"*50)
