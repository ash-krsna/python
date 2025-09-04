#program for accepting a P, T, R values and calculate the simple interest
p = float(input("Enter Principle Amount:"))
t = float(input("Enter Time:"))
r = float(input("Enter Rate of Interest:"))
if(p>0) and (t>0) and (r>0):
    si = (p*t*r)/100
    print("\tSimple Interest is:{}".format(si))
if(p<=0):
    print("\tdont enter -ve or zero principle amount")
if(t<=0):
    print("\tdont enter -ve or zero time")
if(r<=0):
    print("\tdont enter -ve or zero rate of interest")
    
