number_of_turns = int(input())

result = 0
first_range = 0
second_range = 0
third_range = 0
forth_range = 0
fifth_range = 0
fail_range = 0

for turn in range(1, number_of_turns + 1):
    number = int(input())

    if number < 0 or number > 50:
        result /= 2
        fail_range += 1
    elif number < 10:
        result += number * 0.20
        first_range += 1
    elif number < 20:
        result += number * 30 / 100
        second_range += 1
    elif number < 30:
        result += number * 0.40
        third_range += 1
    elif number < 40:
        result += 50
        forth_range += 1
    else:
        result += 100
        fifth_range += 1

print(f"{result:.2f}")

print(f"From 0 to 9: {first_range / number_of_turns * 100:.2f}%")
print(f"From 10 to 19: {second_range / number_of_turns * 100:.2f}%")
print(f"From 20 to 29: {third_range / number_of_turns * 100:.2f}%")
print(f"From 30 to 39: {forth_range / number_of_turns * 100:.2f}%")
print(f"From 40 to 50: {fifth_range / number_of_turns * 100:.2f}%")
print(f"Invalid numbers: {fail_range / number_of_turns * 100:.2f}%")
