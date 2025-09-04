#program for accepting any digit and display its name
d = int(input("Enter Any Digit:"))
if(d==0):
    print("\t{} is Zero".format(d))
else:
    if(d==1):
        print("\t{} is One".format(d))
    else:
        if(d==2):
            print("\t{} is Tow".format(d))
        else:
            if(d==3):
                print("\t{} is Three".format(d))
            else:
                if(d==4):
                    print("\t{} is Four".format(d))
                else:
                    if(d==5):
                        print("\t{} is Five".format(d))
                    else:
                        if(d==6):
                            print("\t{} is Six".format(d))
                        else:
                            if(d==7):
                                print("\t{} is Seven".format(d))
                            else:
                                if(d==8):
                                    print("\t{} is Eight".format(d))
                                else:
                                    if(d==9):
                                        print("\t{} is Nine".format(d))
                                    else:
                                        if(d<0) and d <-9:
                                            print("\t{} is -ve Number".format(d))
                                        else:
                                            if(d>9):
                                                print("\t {} is Postive Number".format(d))
                                            else:
                                                print("\t{} is Invalid Input".format(d))
print("Program Execution Completed")




