#python program to find Area of Circle
while True:
    r = float(input("Enter Radius:"))
    if r < 0:
        print("Enter Correct Radius")
    else:
        a = 3.14*r*r
        b = round(a,2)
        print("Area of Circle:",b)
        break