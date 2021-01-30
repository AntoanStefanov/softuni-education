first_employee_efficency_per_hour = int(input())
second_employee_efficency_per_hour = int(input())
third_employee_efficency_per_hour = int(input())

total_efficiency_per_hour = first_employee_efficency_per_hour + \
    second_employee_efficency_per_hour + third_employee_efficency_per_hour

people_questions = int(input())
total_hours = 0
while True:
    if people_questions <= 0:
        break
    people_questions -= total_efficiency_per_hour
    total_hours += 1
    if total_hours % 4 == 0:
        total_hours += 1

print(f"Time needed: {total_hours}h.")
