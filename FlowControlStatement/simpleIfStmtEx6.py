#Area of Circle
try:
    radius = float(input("Enter Radius:"))
    if radius <= 0:
        print("Enter Appropriate Radius")
    if radius >= 0:
        area = 3.14 *(radius*radius)
        print(f"Area of Circle = {area}")
    print("Program Execution Completed")
except ValueError:
    print("Enter Numbers Only")