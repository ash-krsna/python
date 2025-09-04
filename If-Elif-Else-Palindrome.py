#program for accepting a vlaue and decide whether it is palindrome or not
value = input("Enter Any Value:")
if (value == value[::-1]):
    print("\t{} is Palindrome".format(value))
elif(value != value[::-1]):
    print("\t{} is not palindrome".format(value))
print("Program Execution Completed")
