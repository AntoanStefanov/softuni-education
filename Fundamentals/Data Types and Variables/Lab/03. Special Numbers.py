number = int(input())

# цикъл за колко проверки ще имаме изобщо от 1 до края на числото
for iteration in range(1, number + 1):
    iteration = str(iteration)
    sum_of_digits = 0
    # Цикъл за всяко число и колко цифри има то .
    for digit in iteration:
        sum_of_digits += int(digit)

    if (sum_of_digits == 5) or (sum_of_digits == 7) or (sum_of_digits == 11):
        print(f"{iteration} -> True")
    else:
        print(f"{iteration} -> False")
