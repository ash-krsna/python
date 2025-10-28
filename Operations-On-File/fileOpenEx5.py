try:
    with open("hyd2.data","wt") as fp:
        print("-"*50)
        print("\tFile created and opened in write mode successfully")
        print("\ttype of fp=",type(fp))
        print("\tFile Name =",fp.name)
        print("\tFile Opening Mode=",fp.mode)
        print("\tis File Readable =",fp.readable)
        print("\tis File Writable",fp.writable)
        print("-"*50)
    print("I am out-off with open() as indentations block")
    print("\t is file closed",fp.closed)
except FileNotFoundError:
    print("File does not exist")