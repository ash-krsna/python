s = " "
print('s = " "',s.isspace())
s = "Python Prog"
print('s = "Python Prog"',s.isspace())
s = "Radha Rani"
print('s = "Radha Rani"',s.isspace())
print('s = "Radha Rani"',s.isalpha())
print('s = "Radha Rani"',s.isalpha() or s.isspace())
b = s.isalpha() or s.isspace()
print(b)
