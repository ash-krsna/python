# Program for accepting a number and deciding whether it is prime or not
n = int(input("Enter a number: "))

if n <= 1:
    print("\t{} is invalid input".format(n))
else:
    res = True
    for i in range(2, n):
        if n % i == 0:
            res = False
            break
    print("\t{} is {}".format(n, "PRIME" if res else "NOT PRIME"))