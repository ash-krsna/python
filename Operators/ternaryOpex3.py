#Writea python program which will accept Possitive Numerical value and decide whether it is EVEN or ODD
n = float(input("Enter Any Possitive Numerical Value:"))
res = "EVEN" if (n>0) and (n%2==0) else "ODD" if(n>0) and (n%2!=0) else "Invalid Input"
print("{} is {}".format(n,res))
