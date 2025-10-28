#Program for accepting a numerical value and deside whether it is +VE or -Ve or ZERO
val = float(input("Enter Any Numerical Value:"))
if(val > 0):
    print("\t {} is +VE".format(val))
else:
    if(val < 0):
        print("\t {} is -VE".format(val))
    else:
        print("\t {} is ZERO".format(val))
    print("\tI am from inner if else statement")
print("\t I am from outer if else statement")

          

        