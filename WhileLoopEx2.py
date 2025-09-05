#program for generating 1 to n numbers where N is +ve
n = int(input("Enter how many numbers u want to generate:"))
if(n<0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tNumberes wihing:{}".format(n))
    print("-"*50)
    i=1 #Initialization Part
    while(i<=n): #Condition Part
        print("\t{}".format(i)) #Statement Part
        i=i+1 #Updation Part
    else:
        print("-"*50)

