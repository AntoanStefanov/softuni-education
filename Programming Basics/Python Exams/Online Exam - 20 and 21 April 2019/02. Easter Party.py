number_of_guests = int(input())

cover = float(input())

budget = float(input())

if 10 <= number_of_guests <= 15:
    cover = cover * 0.85
elif 15 < number_of_guests <= 20:
    cover = cover * 0.80
elif number_of_guests > 20:
    cover = cover * 0.75


cake = budget * 0.10

needed_money = (number_of_guests * cover) + cake


if needed_money > budget:
    print(f"No party! {needed_money - budget:.2f} leva needed.")
else:
    print(f"It is party time! {budget - needed_money:.2f} leva left.")
