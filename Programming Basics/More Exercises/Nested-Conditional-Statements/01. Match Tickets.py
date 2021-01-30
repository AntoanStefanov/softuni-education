budget = float(input())
category = input()
people = int(input())


if 1 <= people <= 4:
    transport = budget * 0.75
    left_money = budget - transport
elif 5 <= people <= 9:
    transport = budget * 0.6
    left_money = budget - transport
elif 10 <= people <= 24:
    transport = budget * 0.5
    left_money = budget - transport
elif 25 <= people <= 49:
    transport = budget * 0.4
    left_money = budget - transport
elif people >= 50:
    transport = budget * 0.25
    left_money = budget - transport


if category == "Normal":
    tickets = people * 249.99
elif category == "VIP":
    tickets = people * 499.99

if left_money >= tickets:
    spare_money = left_money - tickets
    print(f"Yes! You have {spare_money:.2f} leva left.")
else:
    money_more = tickets - left_money
    print(f"Not enough money! You need {money_more:.2f} leva.")
