#Program for demonstrating how to write the data to the file
print("-"*50)
sno = int(input("Enter Student Number:"))
sname = input("Enter Studnet Name:")
marks = float(input("Enter Student Marks:"))
print("-"*50)
with open("student1.data","a") as fp:
    fp.write("\n"+ str(sno)+"\t")
    fp.write(sname + "\t")
    fp.write(str(marks)+"\n")
    print("Data written to the file")
