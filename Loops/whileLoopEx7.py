#Programning for calculating sum of first N natural numbers
n = int(input("Enter how many natural numbers of sum you want:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("First {} natural numbers".format(n))
    print("-"*50)
    p = 0 # Additive Identity
    i = 1
    while (i <=n):
        print("\t{}".format(i))
        p = p + i
        i = i + 1
    else:
        print("-"*50)
        print("sum = {}".format(p))
        print("-"*50)
