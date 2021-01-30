first_number = int(input())
second_number = int(input())
third_number = int(input())


for first_digit in range(1, first_number + 1):

    for second_digit in range(2, second_number + 1):
        for digit in range(2, second_digit):
            if second_digit % digit == 0:
                break
        else:
            for third_digit in range(1, third_number + 1):
                if first_digit % 2 == 0 and third_digit % 2 == 0:
                    print(first_digit, second_digit, third_digit)
