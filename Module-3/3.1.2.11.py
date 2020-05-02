wordWithoutVovels = ""

# Prompt the user to enter a word
# and assign it to the userWord variable

userWord = input("Enter a word: ").upper()
for letter in userWord:
    if letter == "A":
        continue
    elif letter == "I":
        continue
    elif letter == "U":
        continue
    elif letter == "E":
        continue
    elif letter == "O":
        continue
    else:
        wordWithoutVovels += letter

print(wordWithoutVovels)
