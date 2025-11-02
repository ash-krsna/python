#Program fro generating N to 1 in reverse order which is positive
n = int(input("Enter how many numbers you want to generate:"))
if(n<=0):
    print("\t {} is invalid input".format(n))
else:
    print('-'*50)
    print("Numbers from {} to 1".format(n))
    print("-"*50)
    for i in range(n, 0, -1):
        print("\t{}".format(i))
    else:
        print("-"*50)