#Program for accepting any digit and display its name
d = int(input("Enter Any Digit:"))
if(d == 0):
    print("\t{} is ZERO".format(d))
else:
    if(d == 1):
        print("\t is ONE".format(d))
    else:
        if(d == 2):
            print("\t {} is TWO".format(d))
        else:
            if(d == 3):
                print("\t{} is THREE".format(d))
            else:
                if(d == 4):
                    print("\t {} is FOUR".format(d))
                else:
                    if(d == 5):
                        print("\t {} is FIVE".format(d))
                    else:
                        if(d == 6):
                            print("\t {} is SIX".format(d))
                        else:
                            if(d == 7):
                                print("\t {} is SEVEN".format(d))
                            else:
                                if(d == 8):
                                    print("\t {} is EIGHT".format(d))
                                else:
                                    if(d == 9):
                                        print("\t {} is NINE".format(d))
                                    else:
                                        if(d<0) and d not in range(-1,-10,-1):
                                            print("\t {} is -VE NUMBER".format(d))
                                        else:
                                            if(d > 9):
                                                print("\t {} is +VE DIGIT".format(d))
                                            else:
                                                if(d < -9 ):
                                                    print("\t {} is -VE DIGIT")
print("Program Execution Completed")

                            
                            


