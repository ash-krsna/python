#program for accepting any digit and display its name
d = int(input("Enter Any Digit:"))
if(d==0):
    print("\t{} is Zero".format(d))
if(d==1):
    print("\t{} is One".format(d))
if(d==2):
    print("\t{} is Two".format(d))
if(d==3):
    print("\t{} is Three".format(d))
if(d==4):
    print("\t{} is Four".format(d))
if(d==5):
    print("\t{} is Five".format(d))
if(d==6):
    print("\t{} is Six".format(d))
if(d==7):
    print("\t{} is Sevem".format(d))
if(d==8):
    print("\t{} is Eight".format(d))
if(d==9):
    print("\t{} is Nine".format(d))
if(d<0) and d < -9:
    print("\t{} is -ve number".format(d))
if(d<0) and d > -10:
    print("\t {} is ve digit".format(d))
print("Program Execution Completed")
