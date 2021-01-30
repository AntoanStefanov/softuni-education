# 1.	Плод - текст с възможности: "Watermelon", "Mango", "Pineapple"
#  или "Raspberry"
# 2.	Размерът на сета - текст с възможности: "small" или "big"
# 3.	Брой на поръчаните сетове - цяло число в интервала [1 … 10000]


fruit = input()

packaging = input()

numbers_of_packaging = int(input())


if packaging == "small":
    if fruit == "Watermelon":
        small_packaging = 2 * 56
    elif fruit == "Mango":
        small_packaging = 2 * 36.66
    elif fruit == "Pineapple":
        small_packaging = 2 * 42.10
    elif fruit == "Raspberry":
        small_packaging = 2 * 20
elif packaging == "big":
    if fruit == "Watermelon":
        big_packaging = 5 * 28.70
    elif fruit == "Mango":
        big_packaging = 5 * 19.60
    elif fruit == "Pineapple":
        big_packaging = 5 * 24.80
    elif fruit == "Raspberry":
        big_packaging = 5 * 15.20
if packaging == "small":
    price = small_packaging * numbers_of_packaging
elif packaging == "big":
    price = big_packaging * numbers_of_packaging


if 400 <= price <= 1_000:
    price -= price * 0.15
elif price > 1_000:
    price -= price * 0.50

print(f"{price:.2f} lv.")
