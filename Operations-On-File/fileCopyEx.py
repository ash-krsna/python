#Program for copying the content of one file into another file
def filecopy():
    try:
        srcfile = input("Enter Source File:")
        with open(srcfile,"r") as rp:
            dstfile = input("Enter Destination Fiel:")
            with open(dstfile,"a") as wp:
                srcfiledata=rp.read()
                wp.write(srcfiledata)
                print("file copied successfully")
    except FileNotFoundError:
        print("Source File does not exist")
#Main Program
filecopy()