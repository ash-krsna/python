#Program for acceptin any file name and display its content
def dispfilecontent():
    try:
        filename = input("Enter any file name:")
        with open(filename,"r") as fp:
            filedata = fp.read()
            print("-"*50)
            if(len(filedata)>0):
                print(filedata)
            else:
                print("File does not contain data")
            print('-'*50)
    except FileNotFoundError:
        print("File does not exist")
#Main program
dispfilecontent()