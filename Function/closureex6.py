
#Program for showing the need of Closures
#ClosureEx7.py
def licpolicy(sumassured): # Outer Function Call--here 'a' is Called Formal parameter
	yearlybonus=8 # Here b is called Local Variable for outer function and global var for inner function
	def yearlybonuscalwithsumassured(pamt): # Inner Function--Closure
		nonlocal yearlybonus
		Total_Amount=sumassured+(sumassured*yearlybonus)/100+pamt
		print("Sum Assured:{} Yearly-Bonus:{} Pamt:{} Total Amount:{}".format(sumassured,yearlybonus,pamt,Total_Amount))
		yearlybonus=yearlybonus+1
	return yearlybonuscalwithsumassured

#Main Program
yb=licpolicy(500000)
print("-"*50)
for i in range(1,16):
	yb(25000)
print("-"*50)
