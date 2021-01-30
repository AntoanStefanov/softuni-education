

def smallest_of_three_numbers(first_number, second_number, third_number):
    smallest = third_number  # Третото е най-малко до доказване на противното.
    if first_number < second_number and first_number < third_number:
        smallest = first_number
    elif second_number < first_number and second_number < third_number:
        smallest = second_number
    return smallest


a = int(input())
b = int(input())
c = int(input())

result = smallest_of_three_numbers(a, b, c)

print(result)
