def get_characters_in_range(start, end):
    string = ""
    for char in range(ord(start) + 1, ord(end)):
        string += (f"{chr(char)} ")
    return string


char_one = input()
char_two = input()


result = get_characters_in_range(char_one, char_two)
print(result)
