vowels = {'a', 'o', 'u', 'e', 'i'}
# Using set beacuse the check for given element is faster than a list.
# And that variable is only for checking.


string = input()


list_with_no_vowels = [
    char
    for char in string
    if char.lower() not in vowels
]
# The Above is equal to [char for char in string if char.lower( not in vowels)]
print(''.join(list_with_no_vowels))
