destination = input()
dates = input()
nights = int(input())


if destination == "France":
    if dates == "21-23":
        night_price = 30
    elif dates == "24-27":
        night_price = 35
    elif dates == "28-31":
        night_price = 40
elif destination == "Italy":
    if dates == "21-23":
        night_price = 28
    elif dates == "24-27":
        night_price = 32
    elif dates == "28-31":
        night_price = 39
elif destination == "Germany":
    if dates == "21-23":
        night_price = 32
    elif dates == "24-27":
        night_price = 37
    elif dates == "28-31":
        night_price = 43
print(f"Easter trip to {destination} : {nights * night_price:.2f} leva.")
