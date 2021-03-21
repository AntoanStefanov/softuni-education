def decimal_to_binary(decimal_number):
    binary_number = []

    while decimal_number > 0:
        digit = decimal_number % 2
        decimal_number = decimal_number // 2
        binary_number.append(str(digit))

    binary_number.reverse()
    return ''.join(binary_number)


number = int(input())

binary_number = decimal_to_binary(number)

if number:
    print(binary_number[-2])
else:
    print(0)

