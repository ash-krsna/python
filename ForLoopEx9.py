#program for calculating sum of squares and cubes of first n natural numbers
n = int(input("Enter how many numbers you want to generate:"))
if(n<=0):
    print("\t{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tSum of squares and cubes of first {} natural numbers".format(n))
    print("-"*50)
    sum_squares = 0
    sum_cubes = 0
    for i in range(1,n+1):
        print("\tNumber: {}, Square: {}, Cube: {}".format(i, i**2, i**3))
        sum_squares += i**2
        sum_cubes += i**3
    else:
        print("-"*50)
        print("\tSum of squares of first {} natural numbers is: {}".format(n, sum_squares))
        print("\tSum of cubes of first {} natural numbers is: {}".format(n, sum_cubes))
        print("-"*50)
