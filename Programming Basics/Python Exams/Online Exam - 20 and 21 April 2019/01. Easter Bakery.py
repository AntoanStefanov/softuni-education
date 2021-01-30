flour_price_kg = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs = int(input())
yeast_packs = int(input())


sugar_price_kg = flour_price_kg * 0.75
eggs_price = flour_price_kg * 1.10
yeast_packs_price = sugar_price_kg * 0.20


flour_total = flour_price_kg * flour_kg
sugar_total = sugar_price_kg * sugar_kg
eggs_total = eggs_price * eggs
yeast_packs_total = yeast_packs_price * yeast_packs

print(f"{flour_total + sugar_total + eggs_total + yeast_packs_total:.2f}")
