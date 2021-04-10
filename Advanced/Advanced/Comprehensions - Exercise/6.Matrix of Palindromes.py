# alphabet = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm',
#             13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
# Better way to generate alphabet:
import string
alphabet = dict(zip(range(26), string.ascii_lowercase))
print(alphabet)

rows, columns = [int(n) for n in input().split()]

matrix_of_palindromes = []

for row in range(rows):
    matrix_of_palindromes.append([])
    for col in range(columns):
        matrix_of_palindromes[row].append('')
        for letter_num in range(3):
            if letter_num == 0 or letter_num == 2:
                matrix_of_palindromes[row][col] += alphabet[row]
            elif letter_num == 1:
                matrix_of_palindromes[row][col] += alphabet[row + col]

[print(' '.join(row)) for row in matrix_of_palindromes]
