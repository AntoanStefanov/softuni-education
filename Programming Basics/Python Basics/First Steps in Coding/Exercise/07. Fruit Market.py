strawberry_price_per_kg = float(input())
banana_quantity_in_kg = float(input())
orange_quantity_in_kg = float(input())
raspberry_quantity_in_kg = float(input())
strawberry_quantity_in_kg = float(input())
raspberry_price_per_kg = strawberry_price_per_kg / 2
orange_price_per_kg = raspberry_price_per_kg - \
    (0.4 * raspberry_price_per_kg)  # (40/100)
banana_price_per_kg = raspberry_price_per_kg - \
    (0.8 * raspberry_price_per_kg)  # (80/100)
total_raspberry = raspberry_quantity_in_kg * raspberry_price_per_kg
total_orange = orange_quantity_in_kg * orange_price_per_kg
total_banana = banana_quantity_in_kg * banana_price_per_kg
total_strawberry = strawberry_quantity_in_kg * strawberry_price_per_kg
money = total_raspberry + total_orange + total_banana + total_strawberry
print(money)
