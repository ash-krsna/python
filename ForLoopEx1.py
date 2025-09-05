#program for generaing 1 to n numbers where n is +ve
n = int(input("Enter how many numbers u want to generate:"))
if(n<0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tNumberes wihing:{}".format(n))
    print("-"*50)
    for i in range(1,n+1):
        print("\t{}".format(i))
    else:
        print("-"*50)
        
