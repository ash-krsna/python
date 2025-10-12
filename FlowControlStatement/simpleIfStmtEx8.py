#Area of Rectangle
try:
    l = float(input("Enter Length:"))
    b = float(input("Enter Breadth:"))
    if b <= 0 and l <= 0:
        print("Enter Valid Input")
    if b >= 0 and l >= 0:
        area = l * b
        print("Area of Rectangle =",area)
    print("Program Execution Completed")
except ValueError:
    print("Enter Numbers Only")