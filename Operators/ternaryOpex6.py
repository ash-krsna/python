#Write a Python Program which will accept any word and check it vowel or not.
word = input("Enter Any Word:")
res = "VOWEL WORD" if ("a" in word or "e" in word or "i" in word or "o" in word or "u" in word or \
                       "A" in word or "E" in word or "I" in word or "O" in word or "U" in word) else "NOT VOWEL WORD"
print("{} is {}".format(word,res))