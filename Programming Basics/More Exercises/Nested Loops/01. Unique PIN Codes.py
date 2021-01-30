first_number_max = int(input())
second_number_max = int(input())
third_number_max = int(input())

for first_number in range(1, first_number_max + 1):
    if first_number % 2 == 0:
        for second_number in range(2, second_number_max + 1):
            for i in range(2, second_number):
                if second_number % i == 0:
                    break
            else:
                for third_number in range(1, third_number_max + 1):
                    if third_number % 2 == 0:
                        print(f"{first_number} {second_number} {third_number}")
