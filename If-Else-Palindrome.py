#Program for accepting a value and decide whether it is palindrome or not
value = input("Enter Any Value:")
if (value == value[::-1]):
    print("\t{} is palindrome".format(value))
else:
    print("\t{} is not palindrome".format(value))
print("Program Execution Completed")
