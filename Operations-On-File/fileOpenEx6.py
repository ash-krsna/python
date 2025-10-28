try:
    with open("D:\\Documents\\hyd3.data","x+") as fp:
        print("-"*50)
        print("\tFile created and opened inwrite mode successfully")
        print("\ttype of fp =",type(fp))
        print("\tis file closed =",fp.closed)
        print("\tFile Name=",fp.name)
        print("\tfile opening mode=",fp.mode)
        print("\tis file readable =",fp.readable)
        print("\tis file writable =",fp.writable)
        print("-"*50)
    print("I am out-off with open() as indentation block")
    print("\t if file closed =",fp.closed)
except FileExistsError:
    print("File already exist-try with new file")