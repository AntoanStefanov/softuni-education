

def length(password):
    if 6 <= len(password) <= 10:
        return True
    else:
        return "Password must be between 6 and 10 characters\n"


def only_letters_and_digits(password):
    for char in password:
        if not char.isalpha() and not char.isdigit():
            return "Password must consist only of letters and digits\n"
    else:
        return True


def minimum_digits(password):
    digit_count = 0
    for char in password:
        if char.isdigit():
            digit_count += 1
    if digit_count < 2:
        return "Password must have at least 2 digits\n"
    else:
        return True


def total_validation(password):
    result = ''

    if length(password) != True:
        result += length(password)
    if only_letters_and_digits(password) != True:
        result += only_letters_and_digits(password)
    if minimum_digits(password) != True:
        result += minimum_digits(password)
    if result == '':
        return "Password is valid"
    else:
        return result


password = input()
res = total_validation(password)
print(res)
