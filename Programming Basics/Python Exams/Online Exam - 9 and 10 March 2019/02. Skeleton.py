control_minutes = int(input())  # Ред 1.	Минути на контролата
control_seconds = int(input())  # Ред 2.	Секунди на контролата
distance_in_meters = float(input())  # Ред 3.	Дължината на улея в метри
# Ред 4.	Секунди за изминаване на 100 метра
second_per_100_meters = int(input())


# Изчисляване на контролата в секунди

control_minutes_in_seconds = control_minutes * 60 + control_seconds

# Изчисляване, колко пъти времето ще намалее

delay_times = distance_in_meters / 120

# Общо намалено време

delay = delay_times * 2.5

# Времето на Марин

marin_time = (distance_in_meters / 100) * second_per_100_meters - delay


if marin_time <= control_minutes_in_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
else:
    print(
        f"No, Marin failed! He was {marin_time - control_minutes_in_seconds:.3f} second slower.")
