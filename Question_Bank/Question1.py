#Python program to interchange first and last elements in a list.
#First Case
lst1 = [1, 2, 3, 4, 5]
a = lst1[4] = 1
b = lst1[0] = 5
print(lst1)
print("-"*50)
#Second Case
lst2 = [1, 2, 3, 4, 5]
c = lst2[0]
d = lst2[4]
a = lst2[4] = c
b = lst2[0] = d
print(lst2)
print("-"*50)
#Third Case
lst3 = [1, 2, 3, 4, 5]
a = lst3[0], lst3[4] = lst3[4], lst3[0]
print(lst3)
print("-"*50)
#Fourth Case
lst4 = [1, 2, 3, 4, 5]
lst4[0], lst4[4] = lst4[4], lst4[0]
print(lst4)
print("-"*50)
#Fifth Case
lst5 = [1, 2, 3, 4, 5]
for i in range(len(lst5)//2):
    if(i == 2 and 3 and 4):
        continue 
    lst5[i], lst5[len(lst5)-1-i] = lst5[len(lst5)-1-i], lst5[i]
print(lst5)
