lili_age = int(input())
washing_machine_price = float(input())
one_toy_price = int(input())

number_of_toys = 0
money = 0
collected_money = 0


for year in range(1, lili_age + 1):
    if year % 2 == 0:
        money += 10
        collected_money += money - 1  # Открадено левче от брат й
    else:
        number_of_toys += 1

money_from_toys = one_toy_price * number_of_toys
collected_money += money_from_toys
difference = abs(collected_money - washing_machine_price)

if collected_money >= washing_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")


############## OR #############


lili_age = int(input())
washing_machine_price = float(input())
one_toy_price = int(input())

number_of_toys = 0
money = 0
collected_money = 0
stolen_money = 0

for year in range(1, lili_age + 1):
    if year % 2 == 0:
        money += 10
        collected_money += money
        stolen_money += 1
    else:
        number_of_toys += 1

money_from_toys = one_toy_price * number_of_toys
collected_money += money_from_toys - stolen_money
difference = abs(collected_money - washing_machine_price)

if collected_money >= washing_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
