#Program for accepting a value and deside whether it is palindrome or not
value = input("Enter Any Value:")
if(value == value[::-1]):
    print("\t{} is Palindrome".format(value))
else:
    print("\t is not Palindrome".format(value))
print("Program Execution Completed")