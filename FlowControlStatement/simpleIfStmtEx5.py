#Program for accepting a P,T,R Values and Calculate simple interest.
try:
    p = float(input("Entere Principle Amount:"))
    t = float(input("Enter Time:"))
    r = float(input("Enter Rate of Interest:"))
    if(p>0) and (t>0) and (r>0):
        si = (p * t * r)/100
        print("\tSimple Interest = {}".format(si))
    if(p<=0):
        print("\t Don't Enter -VE / ZERO value for principle amount")
    if(t<=0):
        print("\t Don't Enter -VE / ZERO value for Time")
    if(r<=0):
        print("\tDon't Enter -VE / ZERO for rate of Interest")
except ValueError:
    print("ValueError")