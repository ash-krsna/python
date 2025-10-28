#Program for reading the data from the file by using readlines()
def fileread():
    print("-"*50)
    with open("hyd1.data","r") as fp:
        filedata = fp.readlines()
        for val in filedata:
            print(val,end=" ")
    print("-"*50)
#main program
fileread()