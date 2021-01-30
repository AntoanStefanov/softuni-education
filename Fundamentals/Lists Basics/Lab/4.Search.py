sentences = int(input())
word = input()
text = []
text_with_word = []
for sentence in range(1, sentences + 1):
    sentence = input()
    text.append(sentence)
    if word in sentence:
        text_with_word.append(sentence)
print(text)
print(text_with_word)
