
#Program for Demonstrating the need of Closure.
#ClosureEx3.py
def  welcome(sname): # Outer Function
	print("I am from Outer function")
	def greet(pname):  # inner Function
		print("'{}''is welcoming to '{}'".format(pname,sname))
	return greet

#Main Program
grt=welcome("Rossum")
grt("Ramesh")
grt("Rakesh")
grt("Raj")
