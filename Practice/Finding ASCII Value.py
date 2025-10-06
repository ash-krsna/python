#Program to print ASCII Value of a character
char = input("Enter Character:")
if len(char)>1:
    input(print("Enter Character Again:"))
elif ord(char) < 65:
    input(print("Enter Alphabets:"))
else:
    print("ASCII Value of Entered character of Yours:{}".format(ord(char)))

