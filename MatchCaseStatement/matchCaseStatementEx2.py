import sys
s = """ -----------------------------------------
                Base Conversion Calculator
        -----------------------------------------  
         I.  Decimal to Binary
             Decimal to Octal
             Decimal to Hexa
        II.  Binary to Decimal
             Binary to Octal
             Binary to Hexa
        III. Octal to Decimal
             Octal to Binary
             Octal to Hexa
        IV.  Hexa to Decimal
             Hexa to Binary
             Hexa to Octal
        v.   Exit
        ------------------------------------------- """
print(s)
ch = input("Enter Your Choice:")
match(ch):
    case "I":
        dv = int(input("Enter Integer Values for converting into binary octal and hexa:"))
        print("\tGiven Decimal Value = {}".format(dv))
        print("\tBin({})={}".format(dv,bin(dv)))
        print("\tOct({})={}".format(dv,oct(dv)))
        print("\tHex({})={}".format(dv,hex(dv)))
    case "II":
        bv = input("Enter Binary Value Preceded with 0b or 0B for converting into Dec. Octal And Hexa")
        print("\tGiven Binary Value = {}".format(bv))
        x = int(bv,2)
        print("\tDec({})={}".format(bv,x))
        print("\tOct({})={}".format(bv,oct(x)))
        print("\tHex({})={}".format(bv,hex(x)))
    case "III":
        ov = input("Enter Octal Value Preceded With 0o Or 0O for converting into Dec, Binary and Hexa:")
        print("\tGiven Octal Value = {}".format(ov))
        x = int(ov,8)
        print("\tDec({})={}".format(ov,x))
        print("\tBin({})={}".format(ov,bin(x)))
        print("\tHex({})={}".format(ov,hex(x)))
    case "IV":
        hv = input("Enter Hexa Dec Value Preceded With 0x or 0X for Converting into Dec, Bin and Oct:")
        print("\tGiven Hexa Dec Value = {}".format(hv))
        x = int(hv,16)
        print("\tDec({})={}".format(hv,x))
        print("\tBin({})={}".format(hv,bin(x)))
        print("\tOct({})={}".format(hv,oct(x)))
    case "V":
        print("\tThank Your For Using Program")
        sys.exit()
    case _:
        print("\tYour Selection Of Operation Is Wrong Try Again")


