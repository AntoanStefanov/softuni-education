pairs = int(input())
current_value = 0
previous_value = 0
are_all_equal = True
max_difference_between_last_two_pairs = 0

for pair in range(1, pairs + 1):
    first_number = int(input())
    second_number = int(input())

    current_value = first_number + second_number

    if pair == 1:
        previous_value = current_value

    if previous_value != current_value:
        are_all_equal = False

    difference_between_last_two_pairs = abs(previous_value - current_value)
    if difference_between_last_two_pairs > max_difference_between_last_two_pairs:
        max_difference_between_last_two_pairs = difference_between_last_two_pairs

    previous_value = current_value
    current_value = 0

if are_all_equal:
    print(f"Yes, value={previous_value}")
else:
    print(f"No, maxdiff={max_difference_between_last_two_pairs}")


# С ЕДИН ВХОД №№№№№№№№№

pairs = int(input())
current_value = 0
previous_value = 0
are_all_equal = True
max_difference_between_last_two_pairs = 0
for i in range(1, (pairs * 2) + 1):
    number = int(input())

    if i % 2 == 0:
        current_value += number
        if i == 2:
            previous_value = current_value
        else:

            if previous_value != current_value:
                are_all_equal = False
        difference_between_last_two_pairs = abs(current_value - previous_value)
        if difference_between_last_two_pairs > max_difference_between_last_two_pairs:
            max_difference_between_last_two_pairs = difference_between_last_two_pairs

        previous_value = current_value
        current_value = 0
    else:
        current_value += number
if are_all_equal:
    print(f"Yes, value={previous_value}")
else:
    print(f"No, maxdiff={max_difference_between_last_two_pairs}")


####### OR #######

pairs = int(input())
previous_value = 0
value = 0
are_all_pairs_equal = True
max_difference_between_last_two_pairs = 0
for pair in range(1, (2*pairs) + 1):
    number = int(input())

    if pair % 2 == 0:
        value += number
        if pair == 2:
            previous_value = value
        else:
            if previous_value != value:
                are_all_pairs_equal = False

        difference_between_last_two_pairs = abs(value - previous_value)
        if difference_between_last_two_pairs > max_difference_between_last_two_pairs:
            max_difference_between_last_two_pairs = difference_between_last_two_pairs

        previous_value = value
        value = 0
    else:
        value += number

if are_all_pairs_equal:
    print(f"Yes, value={previous_value}")
else:
    print(f"No, maxdiff={max_difference_between_last_two_pairs}")
