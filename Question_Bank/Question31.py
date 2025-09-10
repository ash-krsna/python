#python program for sum of number, digits in list
lst = ["ash",2,3,4,"ak",23,'MongoDB']
sum = 0
for i in lst:
    if type(i) == int:
        sum = sum + i
print("sum of numbers in list is:",sum)
