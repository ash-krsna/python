#Program for Demonstrating how to write the data to the file.
itrobj = input("Enter Values:")
with open("Student2.data","a") as fp:
    fp.writelines(str(itrobj)+'\n')
    print("Data Written to the file")