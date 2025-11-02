#Program for generating 1 to N numbers where N is +Ve
n = int(input("Enter how many numbers you want to generate:"))
if(n >= 0):
    print("\t {} is invalid input".format(n))
    print("-"*50)
    for i in range(1, n+1):
        print("\t{}".format(i))
    else:
        print("-"*50)