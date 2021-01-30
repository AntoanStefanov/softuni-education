text = input()

vowel_sum = 0

for position in range(len(text)):
    if text[position] == "a":
        vowel_sum += 1
    elif text[position] == "e":
        vowel_sum += 2
    elif text[position] == "i":
        vowel_sum += 3
    elif text[position] == "o":
        vowel_sum += 4
    elif text[position] == "u":
        vowel_sum += 5

print(vowel_sum)


############## OR ############


text = input()

# буква	a	e	i	o	u
# стойност	1	2	3	4	5
letters_sum = 0

for letter in text:
    if letter == "a":
        letters_sum += 1
    elif letter == "e":
        letters_sum += 2
    elif letter == "i":
        letters_sum += 3
    elif letter == "o":
        letters_sum += 4
    elif letter == "u":
        letters_sum += 5

print(letters_sum)
