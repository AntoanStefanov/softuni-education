words = input().split()
searched_palindrome = input()
palindromes = [word for word in words if word == word[::-1]]
print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")

### OR ###


def is_palindrome(word):
    # връща итератор , за това го запазваме във стринг , за да може да се направи сравнението (string sys string)
    return word == "".join(reversed(word))


words = input().split(" ")
searched_palindrome = input()
# is_palindrome returns True or False
palindromes = [word for word in words if is_palindrome(word)]
print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")

## На един ред функция ###


def is_the_word_palindrome(word): return word == word[::-1]


words = input().split(" ")
searched_palindrome = input()
# is_palindrome returns True or False
palindromes = [word for word in words if is_the_word_palindrome(word)]
print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")
