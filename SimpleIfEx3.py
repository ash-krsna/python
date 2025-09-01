#Write a python program which will calculate area of a square when side value must be positive.
side = float(input("Enter Value of Square Side:"))
if side < 0:
        print("Enter Positive Side Value:")
if side > 0:
            area = side * side
            print("Area of Square is:",area)
print("Program execution completed")
