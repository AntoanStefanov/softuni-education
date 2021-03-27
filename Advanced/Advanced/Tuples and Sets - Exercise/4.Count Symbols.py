from collections import defaultdict
string = input()

symbol_occurrences = defaultdict(int)

for char in string:
    symbol_occurrences[char] += 1

sorted_dict = sorted(symbol_occurrences)

for key in sorted_dict:
    print(f"{key}: {symbol_occurrences[key]} time/s")


########### OR #################

string = input()

symbol_occurrences = defaultdict(int)

for char in string:
    symbol_occurrences[char] += 1

for key, value in sorted(symbol_occurrences.items()):
    print(f"{key}: {value} time/s")

########### OR #################

string = input()

symbol_occurrences = {}

for char in string:
    if char not in symbol_occurrences:
        symbol_occurrences[char] = 0

    symbol_occurrences[char] += 1

sorted_dict = sorted(symbol_occurrences)

for key in sorted_dict:
    print(f"{key}: {symbol_occurrences[key]} time/s")
