# Nested Loops
first_string = input()
second_string = input()

current_string = ""
previous_string = first_string

for iteration in range(len(first_string)):
    for index_str_2 in range(iteration + 1):
        current_string += second_string[index_str_2]
    for index_str_1 in range(iteration + 1, len(first_string)):
        current_string += first_string[index_str_1]
    if not previous_string == current_string:
        print(current_string)
    previous_string = current_string
    current_string = ""
# with slicing

first_word = input()
second_word = input()

mutate_word = ""

for i in range(len(first_word)):
    if first_word[i] == second_word[i]:
        continue
    else:
        mutate_word = second_word[:i+1] + first_word[i+1:]
        print(mutate_word)

####### OR ########
first_string = input()
second_string = input()

string = first_string

for iteration in range(len(first_string)):
    string_1 = first_string[iteration + 1:]
    string_2 = second_string[:iteration + 1]
    if string_2 + string_1 == string:
        continue
    string = string_2 + string_1
    print(string)


# ORRRR ########

first_string = list(input())
second_string = list(input())


index = 0
is_out_of_range = False
while index < len(second_string):

    while first_string[index] == second_string[index]:
        index += 1

        if index == len(second_string):
            is_out_of_range = True
            break

        continue

    if is_out_of_range:
        break

    first_string[index] = second_string[index]
    print(''.join(first_string))
    index += 1

# OR #################################Slice number 2

first = input()
second = input()
for i in range(len(first)):
    if first[i] != second[i]:
        first = first[:i] + second[i] + first[i+1:]
        print(first)


# Гърми Ivan Ivanov и Ivon Vramov otdolu

# First occurance премахва (replace-a)

first_string = input()
second_string = input()


index = 0
is_out_of_range = False
while index < len(second_string):

    while first_string[index] == second_string[index]:
        index += 1

        if index == len(second_string):
            is_out_of_range = True
            break

        continue

    if is_out_of_range:
        break

    first_string = first_string.replace(
        first_string[index], second_string[index], 1)
    print(first_string)
    index += 1
