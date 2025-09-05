#program for accepting a line of text and display each and every letter
s = "PYTHON"
print("-"*50)
print("\t By using for loop-- +ve Indices-- forward direction")
print("-"*50)
for ch in s:
    print("\t{}".format(ch))
print("-"*50)
print("\t By using for loop-- -ve Indices-- backward direction")
print("-"*50)
for ch in s[::-1]:
    print("\t{}".format(ch))
print("-"*50)
print("\t By using for loop-- +ve Indices-- backward direction")
print("-"*50)
for i in range(0,len(s)):
    print("\t{}".format(s[i]))
print("-"*50)
print("\t By using for loop-- -ve Indices-- forward direction")
print("-"*50)
for i in range(-1,(-len(s)+1),-1):
    print("\t{}".format(s[i]))
print("-"*50)
