# •	Името на футболния отбор, за който водим статистика - текст
# •	Броя изиграни срещи през настоящия сезон - цяло число в интервала [0… 100]
#  За всяка изиграна среща се прочита отделен ред:
# o	Резултатът от изиграната среща в един от горепосочените формати – символ с възможности 'W', 'D' и 'L'


club = input()
number_of_games = int(input())
points = 0
wins = 0
draws = 0
loses = 0
for game in range(1, number_of_games + 1):
    result = input()

    if result == "W":
        points += 3
        wins += 1
    elif result == "D":
        points += 1
        draws += 1
    elif result == "L":
        loses += 1

if number_of_games == 0:
    print(f"{club} hasn't played any games during this season.")
else:
    print(f"{club} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print(f"Win rate: {wins / number_of_games:.2%}")
