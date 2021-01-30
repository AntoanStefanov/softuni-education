first_string, second_string = input().split()

min_length = min(len(first_string), len(second_string))

total_sum = 0

for index in range(min_length):
    total_sum += ord(first_string[index]) * ord(second_string[index])


biggest_string = first_string
if len(second_string) > len(first_string):
    biggest_string = second_string


for i in range(min_length, len(biggest_string)):
    total_sum += ord(biggest_string[i])

print(total_sum)
