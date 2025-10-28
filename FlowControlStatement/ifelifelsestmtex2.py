#Program for accepting a numerical value and decide whether it is -+VE or -VE or ZERO
val = float(input("Enter Any Numerical Value:"))
if(val > 0):
    print("\t {} is +VE".format(val))
elif(val < 0):
    print("\t {} is -VE".format(val))
else:
    print("\t {} is ZERO".format(val))
print("I am from outer if else statement")

