#python program to brak list on n range
lst = [1, 'sun',25,3,2,4,'moon',5,'star']
n = int(input("Enter range to break list:"))
a = lst[0:n]
b = lst[n:len(lst)]
print("List before breaking:",lst)
print("List after breaking into two parts:")
print("Part 1:",a)
print("Part 2:",b)
