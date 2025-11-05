s = 'MISSISSIPPI'
print("By using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else part of for loop")
print("-" * 50)

# Today My Req: To display "MISS" without using indexing or slicing
ctr = 0
for chh in s:
    print(chh, end="")       # print each character
    if chh == "S":           # whenever 'S' appears
        ctr += 1
        if ctr == 2:         # after the second 'S', break
            break
else:
    print("I am from else part of for loop")

print("\n" + "-" * 50)
