from bankMenu import menu
from openAccount import openAccount
while(True):
    try:
        menu()
        ch = int(input("Enter Your Choice:"))
        match(ch):
            case 1:
                openAccount()
            case 2: pass
            case 3: pass
            case 4: pass
            case 5: pass
            case 6: pass
            case 7: pass
            case 8:
                print("Thank You for using this program")
                break
            case _:
                print("\t Selection of operation is wrong \n ---Try Again---")
    except ValueError:
        print("\tDont Enter Alphanumeric, Strings, and Symbols for choice \n ---Try Again---")




