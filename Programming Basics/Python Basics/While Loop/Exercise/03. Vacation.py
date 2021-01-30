needed_money = float(input())
money_on_hand = float(input())

days = 0
spend_count = 0

while money_on_hand < needed_money:
    move = input()
    money = float(input())
    days += 1
    if move == "save":
        spend_count = 0
        money_on_hand += money
    if move == "spend":
        money_on_hand -= money
        if money_on_hand < 0:
            money_on_hand = 0
        spend_count += 1
        if spend_count == 5:
            print("You can't save the money.")
            print(f"{days}")
            break


if money_on_hand >= needed_money:
    print(f"You saved the money for {days} days.")


# OR  #


holiday_money = float(input())
balance = float(input())
days = 0
spend_days = 0


while holiday_money > balance:
    action = input()
    money = float(input())
    days += 1
    if action == "spend":
        balance -= money
        if money > balance:
            balance = 0
        spend_days += 1
        if spend_days == 5:
            break

    if action == "save":
        balance += money
        spend_days = 0
if balance >= holiday_money:
    print(f"You saved the money for {days} days.")
else:
    print("You can't save the money.")
    print(days)
