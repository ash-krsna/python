#Write a Python program which will accept any value and decide whether it is Palindrome or Not
value = input("Enter Any Value:")
res = "Palindrome" if value.upper() == value [::-1].upper() else "Not Palindrome"
print("{} is {}".format(value,res))
