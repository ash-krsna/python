#program for accepting a word and decide whether it is vowel word or not
word = input("Enter a word:")
i = 0
decision = "Not a Vowel Word"
while i < len(word):
    if (word[i].lower()) not in list("aeiou"):
        decision = "Vowel Word"
        break
    i += 1
print("\t{} is {}".format(word, decision if decision == "Not a Vowel Word" else "Vowel Word"))
print("-"*50)
