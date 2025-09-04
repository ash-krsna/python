#program for accepting a numerical value and decide whether it is +ve, -ve or zero.
val = float(input("Enter any numerical value:"))
if (val > 0):
    print("\t{} is +ve".format(val))
else:
    if (val<0):
        print("\t{} is -ve".format(val))
    else:
        print("\t{} is zero".format(val))
    print("I am from inner if-else-statement")
print("I am from outer if-else-statement")
