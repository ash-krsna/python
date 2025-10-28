#Program for accepting a numerical value and deside whether it is even or odd
value = float(input("Enter any numerical value:"))
if(value > 0) and (value % 2 == 0):
    print("\t{} is +VE EVEN".format(value))
else:
    if(value > 0) and (value % 2 != 0):
        print("\t {} is +VE ODD".format(value))
    else:
        print("\t{} is Invalid Input".format(value))
print("\tProgram execution completed")