#Python program to find Entered number is Prime or Not.
num = int(input("Enter a number:"))

if num <= 1:
    print("{} is not a prime".format(num))
else:
    prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("{} is not a prime".format(num))
            break
        else:
            print("{} is a prime number".format(num))
