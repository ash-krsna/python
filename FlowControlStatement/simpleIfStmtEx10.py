#Program for accepting any Digit and display it's name
try:
    d = int(input("Enter Any Digit: "))
    if(d == 0):
        print("\t {} is ZERO".format(d))
    if(d == 1):
        print("\t {} is ONE".format(d))
    if(d == 2):
        print("\t {} is TWO".format(d))
    if(d == 3):
        print("\t {} is THREE".format(d))
    if(d == 4):
        print("\t {} is FOUR".format(d))
    if(d == 5):
        print("\t {} is FIVE".format(d))
    if(d == 6):
        print("\t {} is SIX".format(d))
    if(d == 7):
        print("\t {} is SEVEN".format(d))
    if(d == 8):
        print("\t {} is EIGHT".format(d))
    if(d == 9):
        print("\t {} is NINE".format(d))
    if(d<0) and d not in[-1,-2,-3,-4,-5,-6,-7,-8,-9]:
        print("\t{} is -VE NUMBER".format(d))
    if(d<0) and d in range(-1,10,-1):
        print("\t{} is -VE Digit".format(d))
except ValueError:
    print("Enter Numbers Only")