numbers = list(input())
numbers.sort(reverse=True)
largest_number = ""
for number in numbers:
    largest_number += number
print(largest_number)


######### OR ###########

numbers = input()

numbers_list = list(numbers)
sorted_list = sorted(numbers_list, reverse=True)
largest_number = ""
for number in sorted_list:
    largest_number += number
print(largest_number)

# sorted() приема всеки повторяем обект и е функция, докато x.sort() е метод

numbers = list(input())
numbers.sort(reverse=True)
# "" e сеператор между елементите в низа (numbers)
largest_number = "".join(numbers)
print(largest_number)
