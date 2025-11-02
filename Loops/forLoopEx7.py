#Program for generating Multiplicatioin table for a given number where n is +Ve
n = int(input("Enter for generating multiplication table:"))
if(n <= 0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("Multiplication table for:{}".format(n))
    print("-"*50)
    for i in range(1,11):
        print("\t{} X {} = {}".format(n,i,n*i))
    else:
        print('-'*50)
    print('-'*50)
    print("By using while loop")
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("Multiplication Table for: {}".format(n))
    print("-"*50)
    i = 1
    while(i <= 10):
        print("\t{} X {} = {}".format(n,i,n*i))
        i += 1
    else:
        print('-'*50)