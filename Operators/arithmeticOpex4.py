#Program for demonstrating how to dispencing the cash in terms of 500, 200 and 100
wamt = int(input("Enter Withdraw Amount:"))
print("Withdraw Amount:",wamt)
n500 = wamt // 500
wamt = wamt % 500
n200 = wamt // 200
wamt = wamt % 200
n100 = wamt // 100
wamt = wamt % 100
print("-"*50)
print("\tNumber of 500s:".format(n500))
print("\tNumber of 200s:".format(n200))
print("\tNumber of 100s:".format(n100))
print("-"*50)