#pythonp program to print all negative numbers in a range
lst = [-10, -21, 4, -45, 66, -93, 11]
for i in lst[0:len(lst)]:
    if i < 0:
        print(i)
