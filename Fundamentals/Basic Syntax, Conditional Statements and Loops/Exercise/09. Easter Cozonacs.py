budget = float(input())
kg_flour_price = float(input())
pack_of_eggs_price = kg_flour_price * 0.75
liter_milk_price = kg_flour_price * 1.25
quarter_milk_price = liter_milk_price / 4


cozonac_price = pack_of_eggs_price + quarter_milk_price + kg_flour_price

colored_eggs = 0
cozonacs = 0

while budget > cozonac_price:
    budget -= cozonac_price
    cozonacs += 1
    colored_eggs += 3
    if cozonacs % 3 == 0:
        lost_colored_eggs = cozonacs - 2
        colored_eggs -= lost_colored_eggs
print(
    f"You made {cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
