#Write a python program which will calculate area of a triangle where B and H is given and they must be positive.
b = float(input("Enter Base of Triangle:"))
h = float(input("Enter Height of Triangle:"))
if b <= 0 and h <= 0 :
        print("Enter Postive Values:")
if b >= 0 and h >= 0:
            area = 1 / 2 * b * h
            print("Area of Triangle:",area)
print("Program execution completed")
