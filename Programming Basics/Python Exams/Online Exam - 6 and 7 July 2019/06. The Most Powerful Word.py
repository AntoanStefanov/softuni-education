word = input()
best_word = ""
best_points = 0
while word != "End of words":

    is_first_symbol_vowel = False
    first_symbol = word[0]
    first_symbol = first_symbol.lower()
    if first_symbol == "a" or first_symbol == "e" or first_symbol == "i" or first_symbol == "o" or first_symbol == "u" or first_symbol == "y":
        is_first_symbol_vowel = True

    sum_of_symbols = 0

    for symbol in word:
        sum_of_symbols += ord(symbol)

    if is_first_symbol_vowel:
        sum_of_symbols *= len(word)
    else:
        sum_of_symbols //= len(word)

    if sum_of_symbols > best_points:
        best_points = sum_of_symbols
        best_word = word

    word = input()

print(f"The most powerful word is {best_word} - {best_points}")
