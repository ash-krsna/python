#Program for accepting any digit and display its name
dobj = {0 : "ZERO", 1 : "ONE", 2 : "TWO", 3 : "THREE", 4 : "FOUR", 5 : "FIVE", 6:"SIX", 7 : "SEVEN", 8 : "EIGHT", 9 : "NINE"}
d = int(input("Enter Any Digit:"))
res = dobj.get(d) if dobj.get(d) != None else "+VE NUMBER" if d > 9 else "-VE NUMBER" if d < 0 and d not in range (-1,-10,-1) else "-VE DIGIT"
print("\t {} is {}".format(d,res))