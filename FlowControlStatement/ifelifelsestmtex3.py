#Program for accepting a Numerical value and decide whether it is even or odd
value = float(input("Enter Any Numerical Value:"))
if(value > 0) and (value %2 ==0):
    print("\t {} is +VE EVEN".format(value))
elif(value > 0) and (value % 2 != 0):
    print("\t {} is +VE ODD".format(value))
elif(value < 0):
    print("\t {} is Invalid Input".format(value))
print("Program Execution Completed")