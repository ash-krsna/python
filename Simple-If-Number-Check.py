#program for accepting a numerical value and decide wherther it is =ve or zero
val = float(input("Enter Any Numerical Value:"))
if (val > 0):
    print("\t{} is +ve".format(val))
if (val < 0):
    print("\t{} is -ve".format(val))
if (val == 0):
    print("\t{} is zero".format(val))
print("Program Execution completed")


