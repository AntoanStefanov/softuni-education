n = int(input())

for number in range(1111, 10000):
    number = str(number)
    first_two_digits_sum = 0
    second_two_digits_sum = 0
    counter_digits = 0
    for index, digit in enumerate(number):
        if int(digit) == 0:
            pass
        else:
            if index == 0 or index == 1:
                first_two_digits_sum += int(digit)
            if index == 2 or index == 3:
                second_two_digits_sum += int(digit)
            counter_digits += 1
        if first_two_digits_sum == second_two_digits_sum and counter_digits == 4:
            if n % first_two_digits_sum == 0:
                print(number, end=" ")
