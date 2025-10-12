#Program for accepting a Numerical Value and Decide whether It is +VE or -VE or ZERO.
val = float(input("Enter Anu Numerical Value:"))
if(val>0):
    print("\t{} is Possitive".format(val))
if(val<0):
      print("\t{} is Negative".format(val))
if(val == 0):
     print("\t{} is Zero".format(val))
print("Program execution is completed")