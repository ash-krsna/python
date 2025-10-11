
#Program for Demonstrating the need of Closure.
#ClosureEx1.py
def  welcome(sname): # Outer Function
	print("I am from Outer function")
	def greet():  # inner Function
		print("Hi {}: Good Morning".format(sname))
	return greet

#Main Program
grt=welcome("Rossum")
grt()
grt()
grt()
