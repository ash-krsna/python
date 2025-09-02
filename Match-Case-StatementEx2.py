#Write a program which will convert temperature from Celsius to Fahrenheit and vice-versa---|> :)
conversion = """
--------------------------------------------------------
Temperature Conversion--->
1. Celsius to Fahrenheit
2. Celsius to Kelvin 
3. Fahrenheit to Celsius
4. Fahrenheit to Kelvin
5. Kelvin to Fahrenheit
6. Kelvin to Celsius
--------------------------------------------------------
"""
print(conversion)
choice = int(input("Enter your choice(1-6):"))
match choice:
    case 1:
        celsius = float(input("Enter Temperature in Celsius:"))
        fahrenheit = (celsius*(9/5)+32)
        print(f"{celsius}C={fahrenheit}F")
    case 2:
        celsius = float(input("Enter Temperature in Celsius:"))
        kelvin = celsius + 273.15
        print(f"{celsius}C={kelvin}K")
    case 3:
        fahrenheit = float(input("Enter Temperature in Fahrenheit:"))
        celsius = (fahrenheit - 32) * (5/9)
        print(f"{fahrenheit}F={celsius}C")
    case 4:
        fahrenheit = float(input("Enter Temperature in Fahrenheit:"))
        kelvin = (fahrenheit - 32) * (5/9) + 273.15
        print(f"{fahrenheit}F={kelvin}K")
    case 5:
        kelvin = float(input("Enter Temperature in Kelvin:"))
        fahrenheit = (kelvin - 273.15)*(9/5)+32
        print(f"{kelvin}K={fahrenheit}F")
    case 6:
        kelvin = float(input("Enter Temperature is Kelvin:"))
        celsius = kelvin - 273.15
        print(f"{kelvin}K={celsius}C")
    case _:
        print("Your Selection Of Operation Is Wrong Try Again")


    




    


        





        

