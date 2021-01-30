n = int(input())
l = int(input())
for first_number in range(1, n + 1):
    for second_number in range(1, n + 1):
        for third_number in range(97, 97 + l):
            for forth_number in range(97, 97 + l):
                for fifth_number in range(1, n + 1):
                    if fifth_number > first_number and fifth_number > second_number:
                        print(
                            f"{first_number}{second_number}{chr(third_number)}{chr(forth_number)}{fifth_number}", end=" ")
