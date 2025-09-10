#python program to find cumulative sum of a list
lst = [1,2,3,4,5]
sum = 0
cum = []
for i in lst:
    sum = sum + i
    cum.append(sum)
print(cum)
