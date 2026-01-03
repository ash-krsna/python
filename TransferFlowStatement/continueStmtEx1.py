s = "PYTHON"
print("By using for loop")
for ch in s:
    print("I am from else part of for loop")
print("-"*50)
#Today my Req:i want to disp: PYTHON
for ch in s:
    if(ch == "T"):
        continue
    print(ch,end = " ")
else:
    print()