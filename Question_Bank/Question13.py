#python program to find n largest elements from a list
n = int(input("Enter N:"))
lst = [1,2,3,4,5,6,7,8,9,10]
lst.sort(reverse = False)
largest = lst[:n]
print("List in descending order is:",largest)
