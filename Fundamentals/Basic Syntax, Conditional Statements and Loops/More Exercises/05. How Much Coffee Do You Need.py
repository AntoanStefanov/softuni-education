command = input()

special_words = ["cat", "dog", "coding", "movie"]
words = []
coffees = 0

while command != "END":
    words.append(command)
    command = input()

words_in_lowercase = [word for word in words if word.islower()]
words_in_uppercase = [word for word in words if word.isupper()]

for special_word in special_words:
    if special_word in words_in_lowercase:
        coffees += 1
for special_word in words_in_uppercase:
    if special_word.lower() in special_words:
        coffees += 2
if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)
