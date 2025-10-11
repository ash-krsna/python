#python program to find armstrong number
a = int(input("Enter Number:"))
c = str(a)
b = len(c)

sum_of_powers = 0
for d in c:
    sum_of_powers += int(d) ** b 
if sum_of_powers == a:
    print("{} is an Armstrong Number".format(a))
else:
    print("{} is NOT an Armstrong Number".format(a))

    