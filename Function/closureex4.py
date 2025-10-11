#Program for Demonstrating the need of Closure.
#ClosureEx5.py
def  outer(a): # Outer Function--here 'a' is  called Formal Parameter in Outer function
	print("I am from Outer function")
	b=1 # Here 'b' is called Local Variable to outer function and global to inner function
	def inner(c):  # inner Function
		print("I am from inner function")
		print("\ta={}\tb={}\tc={}".format(a,b,c))
	return inner
	

#Main Program
inn=outer(100)
inn(10)
inn(20)
inn(30)
