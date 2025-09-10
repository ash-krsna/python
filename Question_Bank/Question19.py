#python program to print all odd numbers in a range
n = [1,2,3,4,5,6,7,8,9,10]
for i in n[0:len(n)]:
    if i % 2 != 0:
        print(i)
