#python program to print duplicate elements in a list of integers
lst = [1,2,3,4,5,1,2,1,1,1,1,1,1,1,1,100]
dup = []
for i in lst:
    if lst.count(i) > 1:
        if i not in dup:
            dup.append(i)
print(dup)
