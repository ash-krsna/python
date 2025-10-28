#Program for reading the data from the file by using read()
def fileread():
    try:
        with open("emp.pick","r") as fp:
            filedata = fp.read()
            print("-"*50)
            print(filedata)
            print("-"*50)
    except FileNotFoundError:
        print("File does not exist")
#main program
fileread()