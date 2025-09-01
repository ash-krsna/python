#Write a python program which will calculate area of circle by validating radius by using simple if statement.
radius = float(input("Enter Raidus:"))
if radius<0:
        print("Enter Appropriate Radius greater than 0")
if radius>0:
            area = 3.14 * (radius*radius)
            print("Area or circle is:",area)
print("Program Execution Completed")

