#Program for Generating N to 1
n = int(input("Enter How Many Numbers You Want to Generate:"))
if(n<=0):
    print("\t{} Is Invalid Input".format(n))
else:
    print("-"*50)
    print("Numbers From {} to 1".format(n))
    print("-"*50)
    i = n #Init Part
    while(i>=1):
        print("\t{}".format(i))
        i = i - 1 #Or i -=
    else:
        print("-"*50)