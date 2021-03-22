total_price = 0
while True:
    price = input()

    if price == 'special' or price == 'regular':
        break

    price = float(price)

    if price < 0:
        print("Invalid price!")
        continue

    total_price += price

if total_price:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {total_price * 0.20:.2f}$")
    if price == 'special':

        total_price = total_price * 0.90
    print("-----------")
    print(f"Total price: {(total_price + (total_price * 0.20)):.2f}$")
else:
    print('Invalid order!')
