import sys
while (True):
    print("-"*50)
    print("\tArithmetic Operations")
    print("-"*50)
    print("\t1. Addition")
    print("\t2. Subtraction")
    print("\t3. Multiplication")
    print("\t4. Division")
    print("\t5. Floor Division")
    print("\t6. Modulus")
    print("\t7. Exponentiation")
    print("\t8. Exit")
    print("-"*50)
    choice = int(input("Enter Your Choice:"))
    match (choice):
        case 1:
            print("Enter Two Values for addition:")
            a,b = float(input()),float(input())
            print("\tAddition of {} and {} is {}".format(a,b,a+b))
        case 2:
            print("Enter Two Values for Subtraction:")
            a,b = float(input()),float(input())
            print("\tSubtraction of {} and {} is {}".format(a,b,a-b))
        case 3:
            print("Enter Two Values for Multiplication:")
            a,b = float(input()),float(input())
            print("\tMultiplication of {} and {} is {}".format(a,b,a*b))
        case 4:
            print("Enter Two Values for Division:")
            a,b = float(input()),float(input())
            print("\tDivision of {} and {} is {}".format(a,b,a/b))
        case 5:
            print("Enter Two Values for Floor Division:")
            a,b = float(input()),float(input())
            print("\tFloor Division of {} and {} is {}".format(a,b,a//b))
        case 6:
            print("Enter Two Values for Modulus:")
            a,b = float(input()),float(input())
            print("\tModulus of {} and {} is {}".format(a,b,a%b))
        case 7:
            print("Enter Two Values for Exponentiation:")
            a,b = float(input()),float(input())
            print("\tExponentiation of {} and {} is {}".format(a,b,a**b))
        case 8:
            print("Program Execution Completed")
            sys.exit()
        case _:
            print("Invalid Input...Please Try Again")
print("Program Execution Completed")
