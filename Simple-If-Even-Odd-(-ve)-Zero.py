#pogram for accepting a Numerical Value and decide whether it is even or odd
value = float(input("Enter Any Numerical Value:"))
if (value >0 ) and (value % 2 == 0):
    print("\t{} is even".format(value))
if(value > 0) and (value % 2 != 0):
    print("\t{} is odd".format(value))
if (value < 0 ):
    print("\t{} is -ve".format(value))
if (value == 0):
    print("\t{} is zero".format(value))
print("Program Execution Completed")
