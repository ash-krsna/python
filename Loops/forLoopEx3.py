#Program for generating all even numbers within in N where N is +Ve
n = int(input("Enter how many even numbers within the range:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("Even Numbers within: {}".format(n))
    print("-"*50)
    for i in range(2, n+1, 2):
        print("\t {}".format(i))
    else:
        print("-"*50)