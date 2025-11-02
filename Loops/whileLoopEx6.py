#Program for accepting a line of text and display each and every letter
word = "PYTHON"
print("-"*50)
print("By using while loop --> +ve indices <-- forward direction")
print("-"*50)
i = 0
while(i<len(word)):
    print("\t{}".format(word[i]))
    i = i + 1
print("-"*50)
print("By using while loop --> -ve indices <-- forward direction")
print("-"*50)
i =-len(word)
while(i<=-1):
    print("\t{}".format(word[i]))
    i = i + 1
print("By using while loop --> +ve indices <-- backward direction")
print("-"*50)
i = len(word)-1
while(i>=0):
    print("\t{}".format(word[i]))
    i = i -1
print("By using while loop -ve indices --> backward directino")
print("-"*50)
i = -1
while(i>=-len(word[i])):
    print("\t{}".format(word[i]))
    i = i - 1
print("-"*50)
