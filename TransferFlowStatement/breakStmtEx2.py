s = "PYTHON"
print("By using while loop")
i = 0
while i < len(s):
    print("\t{}".format(s[i]))
    i = i + 1
else:
    print("I am from else part of while loop")
print("-" * 50)

# Today my req: to display PYTH without indexing and slicing
i = 0
while i < len(s):
    ch = s[i]
    if ch == "O":     # stop before 'O'
        break
    print(ch, end="")
    i = i + 1
else:
    print("I am from else part of while loop")
print("\n" + "-" * 50)
