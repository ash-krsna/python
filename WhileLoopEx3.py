#program for generating 1 to N numbers where n +ve
n = int(input("Enter How many numbers you want to generate:"))
if(n<0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tNumbers within:{}".format(n))
    print("-"*50)
    i=1 #Initialization Part
    while(i<=n): #Condition Part
        print("\t{}".format(i)) #Statement Part
        i+=1  #Updation Part
    else:
        print("-"*50)
