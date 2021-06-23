### Scroll Down ###

######################## 3 try, 3 except statements #########################

# numbers_dictionary = {}
#
#
# while True:
#     number_as_string = input()
#     if number_as_string == 'Search':
#         break
#     try:
#         number = int(input())
#         numbers_dictionary[number_as_string] = number
#     except ValueError:
#         print("The variable number must be an integer")
#
# line = input()
#
# while line != "Remove":
#     searched = line
#     try:
#         print(numbers_dictionary[searched])
#     except KeyError:
#         print("Number does not exist in dictionary")
#     line = input()
#
# line = input()
#
# while line != "End":
#     searched = line
#     try:
#         del numbers_dictionary[searched]
#     except KeyError:
#         print("Number does not exist in dictionary")
#     line = input()
#
# print(numbers_dictionary)

######################## 1 try, 2 except statements #########################

numbers_dictionary = {}

try:
    while True:
        number_as_string = input()
        if number_as_string == 'Search':
            break
        number = int(input())
        numbers_dictionary[number_as_string] = number

    line = input()

    while line != "Remove":
        searched = line
        print(numbers_dictionary[searched])

        line = input()

    line = input()

    while line != "End":
        searched = line
        del numbers_dictionary[searched]
        line = input()

except ValueError:
    print("The variable number must be an integer")
except KeyError:
    print("Number does not exist in dictionary")

print(numbers_dictionary)
