vowels = ['a', 'o', 'u', 'e', 'i']


string = input()


list_with_no_vowels = [
    char
    for char in string
    if char.lower() not in vowels
]
# The Above is equal to [char for char in string if char.lower( not in vowels)]
print(''.join(list_with_no_vowels))
