#python prgram to find Simple Interest
while True:
    p = float(input("Enter Principle Amount:"))
    r = float(input("Enter Rate:"))
    t = float(input("Enter Time:"))

    if p < 0 :
        print("Enter Correct Amount")
    elif r < 0:
        print("Enter Correct Rate")
    elif t < 0:
        print("Enter Correct Time ")
    else:
        si = (p*r*t)/100
        print("Simple Interest Is:{}".format(si))
        break



