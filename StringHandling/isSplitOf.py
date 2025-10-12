s = "Python is an oop lang"
print('s = "Python is an oop lang"',s.split())
print("Length of s ->",len(s.split()))
x = s.split()
print(x,type(x))
print("Length of x ->",len(x))

d = "12-10-2025"
print(d)
dob = d.split("-") #we can divide this on a particular place by typing this 'd.split("0")' so with the use of this dob is get split on '0'.
print(dob,type(dob))
print("Day",dob[0])
print("Month",dob[1])
print("Year",dob[2])

s = "Apple #Banana #Kiwi / Guava"
words = s.split("#")
print(words)