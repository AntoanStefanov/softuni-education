sea_excursions = int(input())
mountain_excursions = int(input())
no_more_sea = False
no_more_mountain = False

profit = 0

excursion = input()

while excursion != "Stop":

    if not no_more_sea:
        if excursion == "sea":
            sea_excursions -= 1
            profit += 680
            if sea_excursions == 0:
                no_more_sea = True

    if not no_more_mountain:
        if excursion == "mountain":
            mountain_excursions -= 1
            profit += 499
            if mountain_excursions == 0:
                no_more_mountain = True

    if no_more_sea and no_more_mountain:
        print(f"Good job! Everything is sold.")
        break
    excursion = input()

print(f"Profit: {profit} leva.")
