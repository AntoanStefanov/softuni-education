one_number = int(input())
sum_number = 0

while one_number > sum_number:
    number = int(input())
    sum_number += number
print(sum_number)

################# OR ###############

number_limit = int(input())
sum_of_numbers = 0
number = int(input())
while True:
    sum_of_numbers += number
    if sum_of_numbers >= number_limit:
        break
    number = int(input())


print(sum_of_numbers)
