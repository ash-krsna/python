#Program for accepting a line of text and display each and every letter
s = "PYTHON"
print("-"*50)
print("By using for loop in forward direction without indices")
for ch in s:
    print("\t{}".format(ch))
print("-"*50)
print("By using for loop in backward direction without indices")
for ch in s[::-1]:
    print("\t{}".format(ch))
print("-"*50)
print("By using for loop in forward direction with +Ve indices")
for i in range(0, len(s)):
    print("\t{}".format(s[i]))
print("-"*50)
print("By using for loop in forward direction with +Ve indices")
for i in range(len(s)-1,-1,-1):
    print("\t{}".format(s[i]))
print("-"*50)
print("By using for loop in backward direction with -Ve indices")
for i in range(-1, -(len(s)+1),-1):
    print("\t{}".format(s[i]))
print("-"*50)