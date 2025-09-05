#program for accepting a line of text and display each and every letter
word = "PYTHON"
print("-"*50)
print("\t By using while loop-- +ve Indices-- forward direction")
print("-"*50)
i=0 #Initialization Part
while(i<len(word)): #Condition Part
    print("\t{}".format(word[i])) #Statement Part
    i+=1 #Updation Part
    print("-"*50)
print("\t By using while loop-- -ve Indices-- backward direction")
print("-"*50)
i=-len(word)
while(i<=-1): #Condition Part
    print("\t{}".format(word[i])) #Statement Part
    i+=1 #Updation Part
    print("-"*50)
print("\t By using while loop-- +ve Indices-- backward direction")
print("-"*50)
i=len(word)-1 #Initialization Part
while(i>=0): #Condition Part
    print("\t{}".format(word[i])) #Statement Part
    i-=1 #Updation Part
    print("-"*50)
print("\t By using while loop-- -ve Indices-- forward direction")
print("-"*50)
i=-1 #Initialization Part
while(i>=-len(word)): #Condition Part
    print("\t{}".format(word[i])) #Statement Part
    i-=1 #Updation Part
    print("-"*50)
