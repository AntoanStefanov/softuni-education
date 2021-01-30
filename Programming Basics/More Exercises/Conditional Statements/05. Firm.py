from math import floor

needed_hours = int(input())
available_days = int(input())
workers_overtime = int(input())

normal_working_hours = (available_days - (available_days * 0.10)) * 8


overtime_working_hours = workers_overtime * (2 * available_days)


total_working_hours1 = normal_working_hours + overtime_working_hours

total_working_hours = floor(total_working_hours1)


if total_working_hours >= needed_hours:
    left_hours = total_working_hours - needed_hours
    print(f"Yes!{left_hours} hours left.")
else:
    needed_time = needed_hours - total_working_hours
    print(f"Not enough time!{needed_time} hours needed.")
