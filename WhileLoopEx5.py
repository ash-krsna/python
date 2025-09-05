#program for generating all even numbers withing in n where n i +ve
n = int(input("Enter how many numbers you want to generate:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tEven Numbers within:{}".format(n))
    print("-"*50)
    i=1
    while(i<=n): #Condition Part
        if(i%2==0): #Statement Part
            print("\t{}".format(i))
        i=i+1    #Updation Part
    else:
            print("-"*50)
        
