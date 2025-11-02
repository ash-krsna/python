#Program for generating all odd numbers in revers order within the range
n = int(input("Entera the range in which even numbers u want to generate:"))
if(n<=0):
    print("\t {} is invalid input".format(n))
else:
    if(n%2==0):
        n = n - 1
    for i in range(n, 0, -2):
        print("\t{}".format(i))
    else:
        print("-"*50)