#program for accepting a Numerical value and decide whether it is +ve or -ve or zero
val = float(input("Enter Any Numerical Value:"))
if (val >0):
    print("\t{} is +ve number".format(val))
elif(val<0):
    print("\t{} is -ve number".format(val))
else:
    print("\t{} is zero".format(val))
print("I am from outer-if-else statement")
