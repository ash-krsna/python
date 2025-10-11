#Write a Python program which will accept any numerical value and decide whether it is even or odd.
n = float(input("Enter Any Numerical Value:"))
res = "EVEN" if (n%2==0) else "ODD"
print("{} is {}".format(n,res))