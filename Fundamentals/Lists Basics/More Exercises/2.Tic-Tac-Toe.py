first_line = [int(digit) for digit in input().split()]
second_line = [int(digit) for digit in input().split()]
third_line = [int(digit) for digit in input().split()]

ones_indexes = []
twos_indexes = []


def get_indexes(line):
    for index, digit in enumerate(line):
        if digit == 1:
            ones_indexes.append(index)
        elif digit == 2:
            twos_indexes.append(index)


get_indexes(first_line)
get_indexes(second_line)
get_indexes(third_line)


zeros_one = ones_indexes.count(0)
ones_one = ones_indexes.count(1)
twos_one = ones_indexes.count(2)

zeros_two = twos_indexes.count(0)
ones_two = twos_indexes.count(1)
twos_two = twos_indexes.count(2)

if 0 in ones_indexes and 1 in ones_indexes and 2 in ones_indexes:
    print("First player won")

elif zeros_one == 3 or ones_one == 3 or twos_one == 3:
    print("First player won")


elif 0 in twos_indexes and 1 in twos_indexes and 2 in twos_indexes:
    print("Second player won")

elif zeros_two == 3 or ones_two == 3 or twos_two == 3:
    print("Second player won")

else:
    print("Draw!")
