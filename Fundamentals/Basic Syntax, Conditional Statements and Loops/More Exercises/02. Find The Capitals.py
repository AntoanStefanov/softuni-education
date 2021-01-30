string = input()


list_of_indexes = []
for index, symbol in enumerate(string):
    if 65 <= ord(symbol) <= 90:
        list_of_indexes.append(index)

print(list_of_indexes)
