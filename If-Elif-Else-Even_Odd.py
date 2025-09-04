#program for accepting a numerical value and decide whether it is even or odd
value = float(int(input("Enter Any Numerical Value:")))
if(value>0) and ( value%2==0):
    print("\t{} is +ve even number".format(value))
elif(value>0) and ( value%2!=0):
    print("\t{} is +ve odd number".format(value))
elif(value<0):
    print("\t{} is invalid input".format(value))
