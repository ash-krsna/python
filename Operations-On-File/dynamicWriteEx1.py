#Programm for reading the data from key board and write it to the file until we press @
with open("hyd.info","a") as fp:
    print("Enter the information and press @ to stop:")
    while(True):
        kbddata = input()
        if kbddata !="@":
            fp.write(kbddata + "\n")
        else:
            print("Data Written to the file --verify")
            break