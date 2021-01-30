mackerel_price = float(input())  # скумрия
sprat_price = float(input())  # цаца

bonito_kilos = float(input())  # паламуд
scad_kilos = float(input())  # сафрид
mussels_kilos = float(input())  # миди

# •	Паламуд – 60% по-скъп от скумрията

bonito_price_per_kilo = mackerel_price + mackerel_price * 60/100

bonito_price = bonito_price_per_kilo * bonito_kilos

# •	Сафрид – 80% по-скъп от цацата
scad_price_per_kilo = sprat_price + sprat_price * 80/100
scad_price = scad_price_per_kilo * scad_kilos

# •	Миди – 7.50 лв. за килограм

mussels_price = mussels_kilos * 7.50

bill = bonito_price + scad_price + mussels_price
print(f"{bill:.2f}")
