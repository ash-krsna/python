
#Program for Demonstrating the need of Closure.
#ClosureEx6.py
b=1000 # here b is global var
def  outer(a): # Outer Function--here 'a' is  called Formal Parameter in Outer function
	print("I am from Outer function")
	b=1 # Here 'b' is called Local Variable to outer function and global to inner function
	def inner(c):  # inner Function
	nonlocal b
	print("I am from inner function")
	print("\ta={}\tb={}\tc={}".format(a,b,c))
	b=b+1
return inner
	

#Main Program
inn=outer(100)
inn(10)
inn(20)
inn(30)
