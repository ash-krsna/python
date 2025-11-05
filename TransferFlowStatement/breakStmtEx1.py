s = "PYTHON"
print("By using for loop")

for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else part of for loop")

print("_" * 50)

# Today my Req: to display PYTH without using indexing and slicing operations
for ch in s:  # s = "PYTHON"
    if ch == "O":  # Stop when we reach 'O'
        break
    print(ch, end=" ")
else:
    print("I am from else part of for loop")

print("\n" + "-" * 50)
