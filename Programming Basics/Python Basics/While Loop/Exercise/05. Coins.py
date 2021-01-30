change = float(input())  # ресто
coins = 0

change = int(change * 100)  # Защото 0.56 без инт ще е 56.0000000000001 ,
# което не е 56 за компилатора. За това се каства на инт , както се прави със всеки float вход на подобни задачи

coins += change // 200
change = change % 200

coins += change // 100
change = change % 100

coins += change // 50
change = change % 50

coins += change // 20
change = change % 20

coins += change // 10
change = change % 10

coins += change // 5
change = change % 5

coins += change // 2
change = change % 2

if change == 1:
    coins += 1

print(coins)


############# OR ###########

change = float(input())  # ресто

change = int(change * 100)  # Защото 0.56 без инт ще е 56.0000000000001 ,
# което не е 56 за компилатора. За това се каства на инт , както се прави със всеки float вход на подобни задачи
coins = 0
while change > 0:
    if change >= 200:
        change -= 200
        coins += 1
    elif change >= 100:
        change -= 100
        coins += 1
    elif change >= 50:
        change -= 50
        coins += 1
    elif change >= 20:
        change -= 20
        coins += 1
    elif change >= 10:
        change -= 10
        coins += 1
    elif change >= 5:
        change -= 5
        coins += 1
    elif change >= 2:
        change -= 2
        coins += 1
    elif change == 1:
        change -= 1
        coins += 1

print(coins)
