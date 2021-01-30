quantity = int(input())
limit_of_day = int(input())


christmas_spirit = 0
cost = 0
for day in range(1, limit_of_day + 1):
    if day % 11 == 0:  # Отгоре е защото втория 11 ден е 22 , а то се дели на 2 и ако не е отгоре при
        # 12 ред ще влезе без количетството да е увеличено с 2 и дава 60/100 . първо увеличаваме кол.
        quantity += 2

    if day % 2 == 0:
        cost += 2 * quantity
        christmas_spirit += 5
    if day % 3 == 0:
        cost += (5 * quantity) + (3 * quantity)
        christmas_spirit += 13
    if day % 5 == 0:
        cost += 15 * quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        cost += 5 + 3 + 15
        if day == limit_of_day:
            christmas_spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {christmas_spirit}")
