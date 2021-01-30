initial_digit = int(input())
final_digit = int(input())

for first_digit in range(initial_digit, final_digit + 1):
    for second_digit in range(initial_digit, final_digit + 1):
        for third_digit in range(initial_digit, final_digit + 1):
            for forth_digit in range(initial_digit, final_digit + 1):
                if (first_digit % 2 == 0 and forth_digit % 2 == 1) or (first_digit % 2 == 1 and forth_digit % 2 == 0):
                    if first_digit > forth_digit:
                        if (second_digit + third_digit) % 2 == 0:
                            print(
                                f"{first_digit}{second_digit}{third_digit}{forth_digit}", end=" ")
