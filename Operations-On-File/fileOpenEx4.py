try:
    with open("hyd1.data") as fp:
        print("-"*50)
        print("\tFile opened in Read mode successfully")
        print("\tType of fp",type(fp))
        print("\tis File closed",fp.closed)
        print("\tFile Name =",fp.name)
        print("\tFile Opening Mode",fp.mode)
        print("\tIs File Readable =",fp.readable)
        print("\tIs File Writable =",fp.writable)
        print("-"*50)
    print("I am our-off with open() as indentation blok")
    print("\t is file closed",fp.closed)
except FileNotFoundError:
    print("File does not exist")

