s = "python"
print(s.index("p"))
print(s.index("y"))
print(s.index("o"))
print(s.index("n"))
try:
    print(s.index("k"))
except ValueError:
    print("ValueError")
    
