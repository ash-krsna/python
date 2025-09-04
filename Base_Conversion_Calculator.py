import sys
s = """
----------------------------------------------------------
                 Base Conversion Calculator
----------------------------------------------------------
    I. Decimal to Binary
       Deicmal to Octal
       Decimal to Hexadecimal
    II. Binary to Decimal
        Binary to Octal
        Binary to Hexadecimal
    III.Octal to Decimal
        Octal to Binary
        Octal to Hexadecimal    
    IV. Hexadecimal to Decimal
        Hexadecimal to Binary
        Hexadecimal to Octal
    V. Exit
----------------------------------------------------------
"""
print(s)
ch = input("Enter Your Choice:")
match (ch):
    case "I":
        dv = int(input("Enter Integer Values for Converting into Binary, Octal and Hexadecimal:"))
        print("\tGiven Decimal Value = {}".format(dv))
        print("\tBin ({}) = {}".format(dv,bin(dv)))
        print("\tOct ({}) = {}".format(dv,oct(dv)))
        print("\tHex ({}) = {}".format(dv,hex(dv)))
    case "II":
        bv = input("Enter Binary Value for Converting into Decimal, Octal and Hexadecimal:")
        print("\tGiven Binary Value = {}".format(bv))
        x = int(bv,2)
        print("\tDec ({}) = {}".format(bv,x))
        print("\tOct ({}) = {}".format(bv,oct(x)))
        print("\tHex ({}) = {}".format(bv,hex(x)))
    case "III":
        ov = input("Enter Octal Value for Converting into Decimal, Binary and Hexadecimal:")
        print("\tGiven Octal Value = {}".format(ov))
        x = int(ov,8)
        print("\tDec ({}) = {}".format(ov,x))
        print("\tBin ({}) = {}".format(ov,bin(x)))
        print("\tHex ({}) = {}".format(ov,hex(x)))
    case "IV":
        hv = input("Enter Hexadecimal Value for Converting into Decimal, Binary and Octal:")
        print("\tGiven Hexadecimal Value = {}".format(hv))
        x = int(hv,16)
        print("\tDec ({}) = {}".format(hv,x))
        print("\tBin ({}) = {}".format(hv,bin(x)))
        print("\tOct ({}) = {}".format(hv,oct(x)))
    case "V":
        print("Thank for using Program")
        sys.exit()
    case _:
        print("Invalid Input...Please Try Again")
