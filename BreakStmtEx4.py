s = "MISSISSIPPI"
print("By using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else part of for loop")
print("-"*50)
#Today my Req: To display : MISS without using indexing and slicing operations
ctr = 0
for ch in s: # s="MISSISSIPPI"
    if ch == "I":
        ctr += 1
    if ctr == 2:
        break
    print(ch, end="")
else:
    print("\n I am from else part of for loop")
print("\n"+"-"*50)
