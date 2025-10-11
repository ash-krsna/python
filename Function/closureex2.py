
#Program for Demonstrating the need of Closure.
#ClosureEx2.py
def  welcome(sname): # Outer Function
	print("I am from Outer function")
	def greet():  # inner Function
		print("Hi {}: Good Morning".format(sname))
	greet()
	greet()


#Main Program
welcome("Rossum")
