#program for generating N to 1
n = int(input("Enter how many numbers you want to generate:"))
if(n<0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tNumbers within:{}".format(n))
    print("-"*50)
    i=n #Initialization Part
    while(i>=1): #Condition Part
        print("\t{}".format(i)) #Statement Part
        i-=1  #Updation Part
    else:
        print("-"*50)
