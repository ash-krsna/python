n = int(input("Enter Range: "))

# Ensure starting from the largest odd number <= n
if n % 2 == 0:
    i = n - 1
else:
    i = n

print(f"Odd numbers from {n} to 1 are:")
while i >= 1:
    print(f"{i}")
    i -= 2
