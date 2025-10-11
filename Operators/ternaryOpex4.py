#Write a Python prgoram which will accept any numerical value and deicide whether it is +VE ro -VE or ZERO.
n = float(input("Enter Any Numerical Value:"))
res = "+VE" if n>0 else "-VE" if n<0 else "ZERO"
print("{} is {}".format(n,res))