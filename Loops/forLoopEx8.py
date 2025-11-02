#Programming for calculating sum of first N natural numbers
n = int(input("Enter how many natural numbers sum you wnat:"))
if(n<=0):
    print("\t {} is invalid input".format(n))
else:
    print("-"*50)
    print("First {} natural numbers".format(n))
    print('-'*50)
    p = 0 #Additive Indentity
    for i in range(1, n+1):
        print("\t{}".format(i))
        p = p + i
    else:
        print('-'*50)
        print("sum = {}".format(p))
        print("-"*50)

