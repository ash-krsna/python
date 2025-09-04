#program for accepting a numerical value and decide whether it is ever or odd
value = float(input("Enter Any Numerical Value:"))
if(value>0) and (value % 2 == 0):
    print("\t{} is even".format(value))
else:
    if(value>0) and (value % 2 != 0):
        print("\t{} is odd".format(value))
    else:
        print("\t{} is invalid input".format(value))
print("Program Execution Completed")
