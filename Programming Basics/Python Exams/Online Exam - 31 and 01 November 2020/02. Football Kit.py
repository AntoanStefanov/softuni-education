shirt_price = float(input())
needed_money = float(input())

shorts_price = shirt_price * 0.75

socks_price = shorts_price * 0.20

shoes_price = (shirt_price + shorts_price) * 2

total_price = shorts_price + socks_price + shirt_price + shoes_price


total_price -= total_price * 0.15

if total_price >= needed_money:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_price:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {needed_money - total_price:.2f} lv. more.")
