import pickle
with open("emp.pick","rb") as fp:
    print("-"*50)
    while(True):
        try:
            recod = pickle.load(fp)
            for val in recod:
                print("\t{}".format(val),end=" ")
            print()
        except EOFError:
            print("-"*50)
            break