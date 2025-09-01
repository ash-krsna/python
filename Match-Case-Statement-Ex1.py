#Write a program which will implement the following---|
a = """
--------------------------------------------------------
Area of Different Figures--->
C. Circle
R. Rectangle
S. Square
T. Triangle
E. Exit
--------------------------------------------------------
"""
#Here C, R, S, T, E are called case labels...
print(a)
ch = input("Enter Your Choice:")
print("-"*50)
match ch:
    case "C" | "c": 
            print("It's me the Area of Circle:-->")
            r=float(input("Enter Radius Of Circle:"))
            if r<=0:
                  print("Enter Appropritate Radius-->")
                  r=float(input("Enter Radius Of Circle:"))
                  area = 3.14 * r * r
                  print("\t Area of Circle is: {}".format(area))
                  print("-"*50)
            else:
                  if r > 0:
                        area = 3.14 * r * r
                        print("\t Area of Circle is {}".format(area))
                        print("-"*50)
    case "R" | "r": 
            print("It's me the Area of Rectangle:--> ")
            l=float(input("Enter Length of Rectangle:"))
            w=float(input("Enter Width of Rectangle:"))
            if l <= 0 and w > 0 :
                  print("Enter Appropriate Length-->")
                  l=float(input("Enter Length of Rectangle:"))
                  area = l * w
                  print("\tArea of Rectangle: {}".format(area))
                  print("-"*50)
            elif w <= 0 and l > 0:
                  print("Enter Appropriate Width-->")
                  w=float(input("Enter Width of Rectangle:"))
                  area = l * w
                  print("\tArea of Rectangle: {}".format(area))
                  print("-"*50)
            elif l <=0 and w <= 0:
                  print("Entered Value is not Appropriate:(")
                  print("Enter Length and Width Again:)")
                  l = float(input("Enter Length or Rectangle:"))
                  w = float(input("Enter Width of Rectangle:"))
                  area = l * w
                  print("\tArea or Rectangle: {}".format(area))
                  print("-"*50)
            elif l > 0 and w > 0 :
                  area = l * w
                  print("\tArea of Rectangle: {}".format(area))
                  print("-"*50)
        
                  
    case "S" | "s":
            print("It's me The Area of Square-->")
            side = float(input("Enter the Side of Square:"))
            if side <= 0:
                  print("Enter Appropriate Value of Side:(")
                  side = float(input("Enter the Side of Square:"))
                  area = side * side
                  print("\tArea of Square is: {}".format(area))
                  print("-"*50)
            else:
                  area = side * side
                  print("\tArea of Square is: {}".format(area))
                  print("-"*50)
            
    case "T" | "t":
                print("It's me the Area of Triangle-->")
                h = float(input("Enter Height of Triangle:"))
                b = float(input("Enter Base of Triangle:"))
                if h<=0 and b > 0 :
                       print("Enter Appropriate Height of Triangle:(")
                       h = float(input("Enter Height of Triangle:"))
                       area = 1/2 * h * b
                       print("\tArea of Triangle is : {}".format(area))
                       print("-"*50)
                elif b <=0 and h > 0 :
                       print("Enter Appropriate Base of Triangle:(")
                       b = float(input("Enter Base of Triangle:"))
                       area = 1/2 * h * b
                       print("\tArea of Triangle is: {}".format(area))
                       print("-"*50)
                elif h > 0 and b > 0 :
                       area = 1/2 * h * b
                       print("\tArea of Triangle is: {}".format(area))
                       print("-"*50)
                elif h <= 0 and b <= 0  :
                       print("Enter Appropriate Values of Height and Base:(")
                       h = float(input("Enter Height of Triangle:"))
                       b = float(input("Enter Base of Triangle:"))
                       area = 1/2 * h * b
                       print("\tArea of Triangle is: {}".format(area))
                       print("-"*50)
    
    case _: 
              print("You Entered Invalid Choice:(")

print("Program Execution Completed:)")

