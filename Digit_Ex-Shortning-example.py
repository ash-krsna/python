#program for accepting any digit and display its name
dobj={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
a = int(input("Enter Any Digit:"))
res = dobj.get(a) if dobj.get(a)!= None else "+ve number" if a > 9 else "-ve number" if a <0 and a <-9 else "-ve digit"
print("\t{} is {}".format(a,res))
