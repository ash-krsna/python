#python program to remove empty tuples from a list
lst = [(1,2),(),(3,4),(),(5,6),(),()]
for i in lst[0:len(lst)]:
    if i == ():
        lst.remove(i)
print(lst)
