#Program for demonstrating how to write the data to the file
sno = 400
sname = "Jhon"
marks = 86.57
with open("student1.data","a") as fp:
    fp.write(str(sno)+"\t")
    fp.write(sname+"\t")
    fp.write(str(marks)+"\t")
    print("Data written to the file")
