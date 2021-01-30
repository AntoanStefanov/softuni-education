year = input()
holidays = int(input())
hometown_weekends = int(input())


sofia_weekends = 48 - hometown_weekends

volleyball_sofia_saturdays = sofia_weekends * 3/4

volleyball_sofia_holidays = holidays * 2/3

total_volleyball_time = volleyball_sofia_saturdays + \
    volleyball_sofia_holidays + hometown_weekends


if year == "leap":
    additional_volleyball_time = total_volleyball_time * 0.15
    total_volleyball_time += additional_volleyball_time


print(f"{int(total_volleyball_time)}")
