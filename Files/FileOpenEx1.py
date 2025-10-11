#This program demonstrate How to open the file
#FileOpenEx1.py
try:
    fp=open("FileOpenEx1.py")
except FileNotFoundError:
    print("File Does Not Exist")
else:
    print("File opened in Read Mode and we can perform read operations")
    print("Type of fp=",type(fp))
finally:
    print("-"*50)
    print("I am from Finally Block")
    try:
        print("Still file is closed=",fp.closed)
        print("-----------------After Close()-------------------")
        fp.close()
        print("Still file is closed=",fp.closed)
    except NameError:
        print("File Name itself not opened there No Question of closing the file")
    finally:
        ("thx for choosing the files")

