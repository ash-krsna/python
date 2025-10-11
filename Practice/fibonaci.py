#Python Program for n-th Fibonacci number
n = int(input("Enter n:"))
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fiboacci number 1 is 0")
elif n == 2:
    print("Fibonacci number 2 is 1")
else:
    a, b = 0, 1
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    print("fibonacci number {}".format(b))