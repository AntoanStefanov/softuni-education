decimal_number = int(input())
binary_digit = int(input())

binary_number = []

while decimal_number > 0:
    digit = decimal_number % 2
    decimal_number = decimal_number // 2
    binary_number.append(str(digit))


binary_number.reverse()
print(f"{decimal_number} -> {''.join(binary_number)}")
if binary_digit:
    count = binary_number.count('1')
    print(f'We have {count} ones.')
else:
    count = binary_number.count('0')
    print(f'We have {count} zeroes.')
