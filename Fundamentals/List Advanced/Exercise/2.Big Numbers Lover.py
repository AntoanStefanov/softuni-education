numbers = input().split(" ")

numbers.sort(reverse=True)
biggest_number = "".join(numbers)

print(biggest_number)
