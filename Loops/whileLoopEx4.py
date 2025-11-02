#Program for Generating all even numbers within in N where N is +VE
n = int(input("Enter how many even numbers within the range:"))
if(n <= 0 ):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("Even numbers within:{}".format(n))
    print("-"*50)
    i = 1
    while(i<=n):
        if(i % 2 == 0):
            print('\t{}'.format(i))
        i=i+1
    else:
        print("-"*50)
