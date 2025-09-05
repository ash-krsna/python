#program for calculating factorial of a +ve number
n = int(input("Enter a +ve number:"))
if(n<0):
    print("\t{} is invalid input".format(n))
else:
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    else:
        print("-"*50)
        print("\tFactorial of {} is:{}".format(n,fact))
        print("-"*50)
