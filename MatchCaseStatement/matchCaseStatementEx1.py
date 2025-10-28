import sys
while(True):
    print("-"*50)
    print("\tArithmetic Operations")
    print("-"*50)
    print("\t\t1. Addition")
    print("\t\t2. Substraction")
    print("\t\t3. Multiplication")
    print("\t\t4. Division")
    print("\t\t5. Floor Division")
    print("\t\t6. Modules Division")
    print("\t\t7. Exponentation")
    print("\t\t8. Exit")
    print("-"*50)
    ch = int(input("Enter UR Choice:"))
    match (ch):
        case 1 :
            print("Enter Two Values for Addition")
            a,b = float(input()),float(input())
            print("\tsum({},{}) = {}".format(a,b,a+b))
        case 2 :
            print("Enter Two Values for Substraction")
            a,b = float(input()),float(input())
            print("\tsum({},{}) = {}".format(a,b,a-b))
        case 3 :
            print("Enter Two Values for Multiplication")
            a,b = float(input()),float(input())
            print("\tsum({},{}) = {}".format(a,b,a*b))
        case 4 :
            print("Enter Two Values for Division")
            a,b = float(input()),float(input())
            print("\tsum({},{}) = {}".format(a,b,a/b))
        case 5 :
            print("Enter Two Values for Floor Division")
            a,b = float(input()),float(input())
            print("\tsum({},{}) = {}".format(a,b,a//b))
        case 6 :
            print("Enter Two Values for Modules Division")
            a,b = float(input()),float(input())
            print("\tsum({},{}) = {}".format(a,b,a%b))
        case 7 :
            a,b = float(input("Enter Base:")),float(input("Enter Power:")), print("\t Pow({},{}) = {}",format(a,b,a**b))
        case 8 :
            print("\t Thank You For Using This Program")
            sys.exit()
        case _:
            print("\t Your Selection Of Operation is Wrong Try Again")
print("Program Execution Completed")