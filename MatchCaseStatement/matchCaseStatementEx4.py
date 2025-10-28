#Write a Program which will convert temperature from Celsius to Fahrenheit and vice-versa -> :
conversion = """----------------------------------------
                    Temperature Conversion--->
                    1. Celsius to Fahrenheit
                    2. Celsius to Kelvin
                    3. Fahrenheit to Celsius
                    4. Fahrenheit to Kelvin
                    5. Kelvin to Fahrenheit
                    6. Kelvin to Celsius
                ----------------------------------------"""
print(conversion)
choice = int(input("Enter Your Choice(1-5)"))
match choice:
    case 1:
        celsius = float(input("Enter Temperature In Celsius:"))
        fahrenheit = (celsius*(9/5)+32)
        print(f"{celsius} C = {fahrenheit}F")
    case 2:
        celsius = float(input("Enter Temperature in Celsius:"))
        kelvin = celsius+273.15
        print(f"{celsius}C ={kelvin}K")
    case 3:
        fahrenheit = float(input("Enter Temperature in fahrenheit:"))
        celsius = (fahrenheit-32)*(5/9)
        print(f"{fahrenheit}F = {celsius}C")
    case 4:
        fahrenheit = float(input("Enter Temperatue in Fahrenheit:"))
        kelvin = (fahrenheit-32) * (5/9)+273.15
        print(f"{fahrenheit}F = {kelvin}K")
    case 5:
        kelvin = float(input("Enter Temperature in Kelvin:"))
        fahrenheit = (kelvin-273.15)*(9/5)+32
        print(f"{kelvin}K = {fahrenheit}F")
    case 6:
        kelvin = float(input("Enter Temperatue is Kelvin:"))
        celsius = kelvin - 273.15
        print(f"{kelvin}K = {celsius}C")
    case _:
        print("Your Selection of Operation Is Wrong Try Again")

