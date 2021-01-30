ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
average_astronauts_height = float(input())

ship_volume = ship_width * ship_length * ship_height


room_volume = (average_astronauts_height + 0.40) * 2 * 2


astronauts_available = int(ship_volume / room_volume)


if 3 <= astronauts_available <= 10:
    print(f"The spacecraft holds {astronauts_available} astronauts.")
elif astronauts_available < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")
