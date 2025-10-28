try:
    fp = open("hyd2.data")
except FileNotFoundError:
    print("File Does not Exist")
else:
    print("File Opened in read mode and we can perform read operations")
    print("Type of fp=",type(fp))
finally:
    print("-"*50)
    print("I am from finally block")
    try:
        print("Still File is closed=",fp.closed)
        print("-"*50)
        fp.close()
        print("Still file is closed",fp.closed)
    except NameError:
        print("File Name itself not opened-there no question of closing the file")
    finally:("Thank you for using the files:)")
