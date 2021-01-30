wanted_money = float(input())

cocktail = input()
total_price = 0

while cocktail != "Party!":
    coctail_price = len(cocktail)
    number_of_cocktails = int(input())
    order_price = coctail_price * number_of_cocktails
    if order_price % 2 == 1:
        order_price *= 0.75
    total_price += order_price
    if total_price >= wanted_money:
        print("Target acquired.")
        break
    cocktail = input()
else:
    print(f"We need {wanted_money - total_price:.2f} leva more.")
print(f"Club income - {total_price:.2f} leva.")
