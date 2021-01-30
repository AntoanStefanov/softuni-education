words = input().split()

odd_occurrences = {}


for word in words:
    word = word.lower()
    if word not in odd_occurrences:
        odd_occurrences[word] = 0
    odd_occurrences[word] += 1

odd_occurrences_words = []

for word, occurrences in odd_occurrences.items():
    if occurrences % 2 != 0:
        odd_occurrences_words.append(word)

print(" ".join(odd_occurrences_words))
