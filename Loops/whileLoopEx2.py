#Program for Generating 1 to N Numbers where N is +VE
n = int(input("Enter How Many Numbers You Want to Generate:"))
if (n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("\tNumbers Within:{}".format(n))
    print("-"*50)
    i = 1
    while(i<=n): #Condition Part
        print("\t{}".format(i))
        i += 1 #Updation Part <--> here += is called short Hand + Operator
    else:
        print("-"*50)
