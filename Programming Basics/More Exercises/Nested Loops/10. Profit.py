numbers_of_1_coins = int(input())
numbers_of_2_coins = int(input())
numbers_of_5_banknotes = int(input())
profit = int(input())

for coin_of_1 in range(numbers_of_1_coins + 1):
    for coin_of_2 in range(numbers_of_2_coins + 1):
        for banknote_of_5 in range(numbers_of_5_banknotes + 1):
            if (coin_of_1 * 1) + (coin_of_2 * 2) + (banknote_of_5 * 5) == profit:
                print(
                    f"{coin_of_1} * 1 lv. + {coin_of_2} * 2 lv. + {banknote_of_5} * 5 lv. = {profit} lv.")
