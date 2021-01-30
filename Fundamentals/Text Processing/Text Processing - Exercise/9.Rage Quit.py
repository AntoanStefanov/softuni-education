string = input()
message = ''
substring = ''
index = 0
while index < len(string):
    ch = string[index]

    if ch.isdigit():
        number = ch
        if index + 1 < len(string):
            if string[index + 1].isdigit():
                next_number = string[index + 1]
                number += next_number
                index += 1

        message += substring.upper() * int(number)
        substring = ''

    else:
        substring += ch

    index += 1


uniques = set(message)
print(f"Unique symbols used: {len(uniques)}")
print(message)
