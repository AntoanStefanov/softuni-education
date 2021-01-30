from math import ceil
from math import floor

square_meters_vineyard = int(input())

grape_per_square_meter = float(input())

liters_wine_for_sell = int(input())

workers = int(input())


grape = square_meters_vineyard * grape_per_square_meter

grape_for_wine = grape * 0.4

made_wine = grape_for_wine / 2.5

if made_wine >= liters_wine_for_sell:
    remainder_wine = made_wine - liters_wine_for_sell
    wine_for_worker = remainder_wine / workers
    # Резултатът трябва да е закръглен към по-ниско цяло число
    print(
        f"Good harvest this year! Total wine: {floor(made_wine)} liters.")
    # И двата резултата трябва да са закръглени към по-високото цяло число
    print(f"{ceil(remainder_wine)} liters left -> {ceil(wine_for_worker)} liters per person.")

else:
    needed_wine = liters_wine_for_sell - made_wine
    # Резултатът трябва да е закръглен към по-ниско цяло число
    print(
        f"It will be a tough winter! More {floor(needed_wine)} liters wine needed.")
