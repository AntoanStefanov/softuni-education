def vowel_filter(function):

    def wrapper():
        res = function()
        return [ch for ch in res if ch.lower() in ('a', 'e', 'i', 'o', 'u', 'y')]

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

# up same as ::: get_letters = vowel_filter(get_letters)

print(get_letters())
