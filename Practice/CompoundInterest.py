#python program to find Compound Interest
while True:
    p = float(input("Enter Principle Amount:"))
    r = float(input("Enter Rate:"))
    n = float(input("Enter Compounding Number:"))
    t = float(input("Enter Time:"))


    if p < 0 :
        print("Enter Correct Amount")
    elif r < 0:
        print("Enter Correct Rate")
    elif t < 0:
        print("Enter Correct Time ")
    elif n < 0:
        print("Enter Correct Number Of Compound")
    else:
        a = p * (1 + (r/100)/n)**(n*t)
        b = round(a,2)
        print("Simple Interest Is:{}".format(b))
        break



