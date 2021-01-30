first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
answers = int(input())

answers_per_hour = first_employee + second_employee + third_employee
needed_hours = 0

while answers > 0:

    answers -= answers_per_hour
    needed_hours += 1

    if needed_hours % 4 == 0:
        needed_hours += 1

print(f"Time needed: {needed_hours}h.")


