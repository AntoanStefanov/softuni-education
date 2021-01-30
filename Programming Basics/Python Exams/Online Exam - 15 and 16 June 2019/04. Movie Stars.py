budget = float(input())

name = input()

while name != "ACTION":
    if len(name) > 15:
        salary = budget * 0.20
    else:
        salary = float(input())
    if salary > budget:
        print(f"We need {salary - budget:.2f} leva for our actors.")
        break
    budget -= salary
    name = input()
else:
    print(f"We are left with {budget:.2f} leva.")
