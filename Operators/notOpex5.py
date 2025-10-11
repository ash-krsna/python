a = 10 and 30 and 30 or 40
print(f"10 and 30 and 30 or 40 = {a}")
b = 10 and 30 or 40 and not 100 or 45
print(f"10 and 30 or 40 and not 100 or 45 = {b}")
c = "F" and "T" or not "T" or "F" and "T" and not "s"
print(f'"F" and "T" or not "T" or "F" and "T" and not "s" ={c}')
d = not "and"
print('not "and" = {}'.format(d))
try:
    e = eval("not not")
except SyntaxError:
    print("not not --> Invalid Syntax")