#Area of Square
try:
    side = float(input("Enter side of square:"))
    if side <= 0:
        print("Appropriate side length needed:")
    if side >= 0:
        area = side * side
        print(f"Area of Square who have side ={side} area is ={area}")
except ValueError:
    print("Enter Numbers Only")