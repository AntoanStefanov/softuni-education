def get_letter_position_in_alphabet(letter):
    position = ord(letter) - 64  # До доказване на противното

    if letter.islower():
        position = ord(letter) - 96

    return position


def calculate_string_result(string):

    first_letter = string[0]
    last_letter = string[-1]
    number = int(string[1:-1])

    first_letter_position = get_letter_position_in_alphabet(first_letter)
    last_letter_position = get_letter_position_in_alphabet(last_letter)

    result = 0

    if first_letter.isupper():
        result = number / first_letter_position
    else:
        result = number * first_letter_position

    if last_letter.isupper():
        result -= last_letter_position
    else:
        result += last_letter_position

    return result


strings = input().split()
total_sum = 0
for string in strings:
    res = calculate_string_result(string)
    total_sum += res

print(f"{total_sum:.2f}")
