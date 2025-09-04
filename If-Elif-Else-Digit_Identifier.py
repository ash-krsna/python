#program for accepting any digit and display its name
a = int(input("Enter Any Digit:"))
if(a==0):
    print("\t{} is Zero".format(a))
elif(a==1):
    print("\t{} is One".format(a))
elif(a==2):
    print("\t{} is Two".format(a))
elif(a==3):
    print("\t{} is Three".format(a))
elif(a==4):
    print("\t{} is Four".format(a))
elif(a==5):
    print("\t{} is Five".format(a))
elif(a==6):
    print("\t{} is Siz".format(a))
elif(a==7):
    print("\t{} is Seven".format(a))
elif(a==8):
    print("\t{} is Eight".format(a))
elif(a==9):
    print("\t{} is Nine".format(a))
elif(a>9):
    print("\t{} is Positive Number".format(a))
elif(a<-9):
    print("\t{} is Negative Number".format(a))
else:
    print("\t{} is negative digit".format(a))
