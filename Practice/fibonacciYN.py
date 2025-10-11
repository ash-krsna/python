num = int(input("Enter a number:"))
f = "Fibonacci"

a, b = 0, 1
if num == 0 or num == 1:
    print("{} is a {}".format(num,f))
else:
    while b < num:
        a, b = b, a+ b
    if b == num:
        print("{} is a {} number".format(num,f))
    else:
        print("{}is NOT a {} number".format(num,f))
        