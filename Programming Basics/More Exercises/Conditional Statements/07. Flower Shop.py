# •	Магнолии – 3.25 лева
# •	Зюмбюли – 4 лева
# •	Рози – 3.50 лева
# •	Кактуси – 8 лева
# От общата сума, Мария трябва да плати 5% данъци.
import math
numbers_flower_1 = int(input())
numbers_flower_2 = int(input())
numbers_flower_3 = int(input())
numbers_flower_4 = int(input())

gift_price = float(input())

total_money = numbers_flower_1 * 3.25 + numbers_flower_2 * \
    4 + numbers_flower_3 * 3.50 + numbers_flower_4 * 8

money = total_money - total_money * 0.05

if money >= gift_price:
    left = money - gift_price
    print(f"She is left with {math.floor(left)} leva.")
else:
    needed = gift_price - money
    print(f"She will have to borrow {math.ceil(needed)} leva.")
