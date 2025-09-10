#python program to print positive numbers in a list
lst = [-10, -21, 4, -45, 66, -93, 11]
for i in lst[0:len(lst)]:
    if i >= 0:
        print(i)    
print("-"*50)
#python program to print negative numbers in a list        
for i in lst[0:len(lst)]:
    if i <= 0:
        print(i)    
print("-"*50)
