word = input()

for position in range(len(word) - 1, -1, -1):
    print(word[position], end="")


######## OR ######


word = input()

for symbol in reversed(word):
    print(symbol, end="")
