def dispstudent(sno,sname,marks,crs = "PYTHON"):
	print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))
	
#main program
print("-"*50)
print("\tSNO\tName\tMARKS\tCOURSE")
print("-"*50)
dispstudent(100,"RS",45.67)
dispstudent(200,"TR",65.17)
dispstudent(300,"DR",25.17)
dispstudent(100,"JS",65.56)

