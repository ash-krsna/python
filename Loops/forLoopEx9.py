#Programming for calculating sum of squaresand cubes of first nnatural numbers.
n = int(input("Enter how many natural number of sum you want:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("Natural numbers \t\t squares \t\t cubes")
    print("-"*50)
    s,ss,cs=0,0,0
    for i in range(1,n+1):
        print("\t\t{}\t\t{}\t\t{}".format(i,i**2,i**3))
        s = s + i
        ss = ss + i**2
        cs = cs + i**3
    else:
        print("-"*50)
        print("\t\t{}\t\t{}\t\t{}".format(s,ss,cs))
        print("-"*50)