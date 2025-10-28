import pickle
def saveempdata():
    with open("emp.pick","ab") as fp:
        while(True):
            print("-"*50)
            empno=int(input("Enter employee number:"))
            empname=input("Enter Employee Name:")
            empsal=float(input("Enter Employee Salary:"))
            print("-"*50)
            lst = list()
            lst.append(empno)
            lst.append(empname)
            lst.append(empsal)
            
            pickle.dump(lst,fp)
            print("employee data saved as record in file successfully")
            print("-"*50)
            ch = input("Do you want to enter another employee details (yes/no):")
            if(ch.lower()=="no"):
                print("Thank you for using this program")
                break
            print("-"*50)
#Main Program
saveempdata()
                        