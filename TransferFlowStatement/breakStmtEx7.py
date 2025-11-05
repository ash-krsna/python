# Program for accepting a word and deciding whether it is a vowel word or not

word = input("Enter a word: ")
i = 0
decision = "NOT Vowel Word"

while i < len(word):
    if word[i].lower() in "aeiou":  # check each character
        decision = "Vowel Word"
        break
    i = i + 1

print("{} is {}".format(word, decision))
