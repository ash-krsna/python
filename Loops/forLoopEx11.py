#Programming for calculating factorial of given +ve number
n = int(input("Enter number for cal factorial:"))
if(n<0):
    print("{} is invalid input".format(n))
else:
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    else:
        print("Factorial({}) = {}".format(n,fact))