number_of_days = int(input())  # Брой дни
number_of_hours_per_day = int(input())  # Брой часове за всеки един от дните

total_price = 0
for days in range(1, number_of_days + 1):
    total_price_per_day = 0
    for hours in range(1, number_of_hours_per_day + 1):
        if days % 2 == 0 and hours % 2 == 1:  # четен ден и нечетен час
            price = 2.50
        elif days % 2 == 1 and hours % 2 == 0:  # нечетен ден и четен час
            price = 1.25
        else:
            price = 1  # всички останали случаи
        total_price_per_day += price
    total_price += total_price_per_day
    print(f"Day: {days} - {total_price_per_day:.2f} leva")
print(f"Total: {total_price:.2f} leva")
