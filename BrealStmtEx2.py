s = "PYTHON"
print("By using while loop")
i = 0
while i < len(s):
    print("\t{}".format(s[i]))
    i += 1
else:
    print("I am from else part of while loop")
print("-"*50)
#Today my Req: To display : PYTH without using indexing and slicing operations
i = 0
while i < len(s): # s="PYTHON"
    if s[i] == "O":
        break
    print(s[i], end="")
    i += 1
else:
    print("\n I am from else part of while loop")
print("\n"+"-"*50)
