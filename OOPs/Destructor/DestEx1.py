import time
class employee:
    def __init__(self, eno, ename):
        print("I am from parameterized constructor: {}".format(id(self)))
        self.eno = eno
        self.ename = ename
        print("\tEmp Number={}".format(self.eno))
        print("\tEmp Name={}".format(self.ename))
        print("-"*50)
    def __del__(self):
        print("GC calls __del__() for De-Allocating the memory space: {}".format(id(self)))
#main program
print("Program Execution Started")
e1 = employee(100,"RS") #object creation
e2 = employee(200,"JK") #object creation
e3 = employee(300,"MK") #object creation
print("Program Execution Ended")
time.sleep(5)