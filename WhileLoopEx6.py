#program for generating all even numbers within in N where N is +ve
n = int(input("Enter how many numbers you want to generate:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tEven Numbers within:{}".format(n))
    print("-"*50)
    i=2
    while(i<=n): #Condition Part
        print("\t{}".format(i)) #Statement Part
        i+=2    #Updation Part
    else:
            print("-"*50)
