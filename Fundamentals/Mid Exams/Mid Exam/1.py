needed_budget = float(input())
months = int(input())

saved_money = 0


for month in range(1, months + 1):
    if month % 4 == 0:
        saved_money += saved_money * 0.25

    if not month % 2 == 0 and not month == 1:
        spent_money = saved_money * 0.16
        saved_money -= spent_money

    money = needed_budget * 0.25
    saved_money += money


if saved_money >= needed_budget:
    print(
        f'Bravo! You can go to Disneyland and you will have {saved_money-needed_budget:.2f}lv. for souvenirs.')
else:
    print(f'Sorry. You need {needed_budget- saved_money:.2f}lv. more.')
