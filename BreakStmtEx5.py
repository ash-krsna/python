#program for accepting a number and decide whether it is prime or not
n = int(input("Enter a number:"))
if n <= 1:
    print("\t{} is neither prime nor composite".format(n))
else:
    res = "PRIME"
    for i in range(2, n):
        if n % i == 0:
            res = "NOT PRIME"
            break
    else:
        print("I am from else part of for loop")
    print("\t{} is {}".format(n, res))
print("-"*50)
