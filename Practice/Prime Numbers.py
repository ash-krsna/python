#Python Program to find prime number.
start = int(input("Enter Start:"))
end = int(input("Enter end:"))

print("Prime number between {} and {}".format(start,end))


for i in range(start, end+1):
    if i > 1:
        for a in range(2, int(i**0.5)+1):
            if a % i == 0:
                break
    
        else:
            print(i, end=" ")

