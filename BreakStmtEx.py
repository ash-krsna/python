s = "PYTHON"
print("By Using for Loop")
for ch in s:
        print("I am from else part of for loop")
print("-"*50)
#Today my Req: To display : PYTH without using indexing and slicing operations
for ch in s: # s="PYTHON"
    if(ch=="O"):
        break
    print(ch, end="")
else:
    print("\n I am from else part of fsor loop")
print("\n"+"-"*50)  
