#Area of Triangle
try:
    base = float(input("Enter Value of Base:"))
    height = float(input("Enter Value of Height:"))
    if base <= 0 or height <= 0:
        print("Enter Valid inputs")
    if base >=0 and height >= 0:
        area = (1/2)*base*height
        print(f"Area of Traingle is = {area}")
    print("Program Execution Completed")
except ValueError:
    print("Enter Numbers Only")