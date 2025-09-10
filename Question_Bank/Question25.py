#python program to remove empty list from a list
lst = [5,6,[],3,[],[],9]
for i in lst:
    if i == []:
        lst.remove(i)
for i in lst:
    if i == []:
        lst.remove(i)

print(lst)


