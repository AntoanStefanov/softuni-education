number_of_days = int(input())
number_of_hours_for_day = int(input())
price_for_day = 0
total_price = 0
for day in range(1, number_of_days + 1):
    price_for_day = 0
    for hour in range(1, number_of_hours_for_day + 1):
        if day % 2 == 0 and hour % 2 == 1:
            price_for_hour = 2.50
        elif day % 2 == 1 and hour % 2 == 0:
            price_for_hour = 1.25
        else:
            price_for_hour = 1
        price_for_day += price_for_hour
    print(f"Day: {day} - {price_for_day:.2f} leva")
    total_price += price_for_day
print(f"Total: {total_price:.2f} leva")
