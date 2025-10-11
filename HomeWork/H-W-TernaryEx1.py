#Write a python program which will accept any two numerical values decide and find max value and check for equality.
a = float(input("Enter First Value:"))
b = float(input("Enter Second Value:"))
maxval = "a is greater" if (a > b) else "b is greater" if (a != b) else "Both are equal"
print(maxval)
