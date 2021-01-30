###### Basics #####

first_number = int(input())
second_number = int(input())
third_number = int(input())
forth_number = int(input())

sum_of_first_and_second_number = first_number + second_number
division = sum_of_first_and_second_number // third_number
result = division * forth_number
print(result)

######## LIST ########
numbers_in_list = []

for integer in range(4):
    number = int(input())
    numbers_in_list.append(number)

the_sum = numbers_in_list[0] + numbers_in_list[1]
division = the_sum // numbers_in_list[2]
result = division * numbers_in_list[3]
print(result)

######### FUNCTION ########


# PARAMETERS (A parameter is the input that you define for your function)
def integer_operations(first_int, second_int, third_int, forth_int):
    the_sum = first_int + second_int
    division = the_sum // third_int
    result = division * forth_int
    print(result)


# ARGUMENTS (An argument is the actual value for a given parameter)
integer_operations(int(input()), int(input()), int(input()), int(input()))
