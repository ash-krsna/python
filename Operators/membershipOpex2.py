lst = [100,"Rossum",23.45,2+3j]
print(lst)
print("Ros in lst =>","Ros" in lst)
print("Ros in lst[1] =>","Ros" in lst[1])
try:
    print("2+3j in lst[-1]",2+3j in lst[-1])
except TypeError:
    print("2+3j in lst[-1] => TypeError")
try:
    print("(2+3j).real in lst[-1].real",(2+3j).real in lst[-1].real)
except TypeError:
    print("(2+3j).real in lst[-1].real => TypeError")
print("2+3j in lst",2+3j in lst)

