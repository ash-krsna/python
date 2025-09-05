#program for generating Multiplication Table of N given Number where N is +ve
n = int(input("Enter how many numbers you want to generate:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tMultiplication Table of :{}".format(n))
    print("-"*50)
    for i in range(1,11):
        print("\t{} X {} = {}".format(n,i,n*i))
    else:
            print("-"*50)
if n<=0:
    print("\t{} is invalid input".format(n))
else:
     print("-"*50)
     print("\tMultiplication Table of :{}".format(n))
     print("-"*50)
     i=1
     while(i<=10):
        print("\t{} X {} = {}".format(n,i,n*i))
        i+=1
     else:
        print("-"*50)
     
