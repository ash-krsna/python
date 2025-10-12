#Program for accepting a Numerical value and decide whether it is even or odd.
try:
    value = float(input("Enter any numerical value:"))
    if(value>0) and (value % 2 == 0):
        print("\t{} is EVEN".format(value))
    if(value>0) and (value % 2 != 0):
        print("\t{} is ODD".format(value))
    if(value<0):
        print("\t{} is invalid input".format(value))
    print("Program Execution Completed")
except ValueError:
    print("ValueError is interupting please enter numbers only.")