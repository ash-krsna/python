#Program for Generating all even numbers within in N where N is +Ve
n = int(input("Enter how many even numbers within the range:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("Even numbers within:{}".format(n))
    i = 2
    while(i<=n):
        print("\t{}".format(i))
        i+=2
    else:
        print("-"*50)