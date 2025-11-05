# Program for accepting a number and deciding whether it is prime or not

n = int(input("Enter a number: "))

if n <= 1:
    print("{} is not a prime number".format(n))
else:
    res = "PRIME"
    for i in range(2, n):
        if n % i == 0:
            res = "NOT PRIME"
            break  # exit loop if divisor is found
    print("{} is {}".format(n, res))
