string_of_numbers = input()
list_of_numbers = string_of_numbers.split()
list_of_inverted_values = []
for number in list_of_numbers:
    number = - int(number)
    list_of_inverted_values.append(number)
print(list_of_inverted_values)


### OR ###


numbers = [-int(num) for num in input().split()]
print(numbers)