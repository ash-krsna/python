s = "MISSISSIPPI"
print("By using while loop")
i = 0
while i < len(s):
    print("\t{}".format(s[i]))
    i += 1
else:
    print("I am from else part of while loop")

print("-" * 50)

# Today my req: To display MISS without indexing and slicing operations
ctr = 0
i = 0
while i < len(s):
    ch = s[i]
    print(ch, end="")   # print each letter
    if ch == "S":       # whenever 'S' appears
        ctr += 1
        if ctr == 2:    # after the second 'S', stop
            break
    i += 1
else:
    print("I am from else part of while loop")

print("\n" + "-" * 50)
