#Python Program for cube sum of first n natural numbers
num = int(input("Enter Length:"))
sum = 0
for i in range(0,num+1):
    b = i ** 3 
    print("{} X 3 = {}".format(i,b))
    sum = sum + i
print("Sum of First Natural Numbers",sum)
  